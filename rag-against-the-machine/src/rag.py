"""RAG pipeline over the vLLM codebase: index, search, answer, evaluate."""
import re
import sys
from pathlib import Path
from typing import Any, List

import bm25s
import fire
import numpy as np
import Stemmer
from bm25s.stopwords import STOPWORDS_EN_PLUS
from langchain_text_splitters import Language, RecursiveCharacterTextSplitter
from pydantic import BaseModel
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer

from .models import (AnsweredQuestion, MinimalAnswer, MinimalSearchResults,
                     MinimalSource, RagDataset, StudentSearchResults,
                     StudentSearchResultsAndAnswer, UnansweredQuestion)

MODEL = "Qwen/Qwen3-0.6B"
CONTEXT_TOKENS = 4096
PROMPT = ("You answer questions about the vLLM codebase. Use only the "
          "provided context and answer concisely. If the context does not "
          "contain the answer, say so.")
STEMMER = Stemmer.Stemmer("english")
STOPWORDS = set(STOPWORDS_EN_PLUS)
# Fire parses CLI values as Python literals ("a, b" becomes a tuple):
# keep queries and paths as typed, numbers are converted with int().
RAW_TEXT = fire.decorators.SetParseFn(str)


def char_kind(char: str) -> str:
    """Classify a character for identifier splitting.

    Args:
        char: The character to classify.

    Returns:
        "upper" or "lower" for an ASCII letter, "digit" for a digit, else
        "other".
    """
    if "A" <= char <= "Z":
        return "upper"
    if "a" <= char <= "z":
        return "lower"
    return "digit" if char.isdecimal() else "other"


def split_identifier(word: str) -> List[str]:
    """Split an identifier into its snake_case and camelCase parts.

    For example, "load_lora" gives "load" and "lora", and "HTTPServer2"
    gives "HTTP", "Server" and "2". Other characters are separators.

    Args:
        word: The identifier to split.

    Returns:
        The list of parts.
    """
    parts: List[str] = []
    current = ""
    for i, char in enumerate(word):
        kind = char_kind(char)
        previous = char_kind(word[i - 1]) if i > 0 else "other"
        following = char_kind(word[i + 1]) if i + 1 < len(word) else "other"
        # The "e" of "Server" continues the part started by its capital.
        capitalized = previous == "upper" and kind == "lower"
        # The "S" of "HTTPServer" starts a new part: a lowercase letter follows
        new_capital = kind == "upper" and following == "lower"
        if not capitalized and (kind != previous or new_capital) and current:
            parts.append(current)
            current = ""
        if kind != "other":
            current += char
    if current:
        parts.append(current)
    return parts


def tokenize(text: str) -> List[str]:
    """Turn text into stemmed lowercase BM25 tokens.

    Identifiers are kept whole and also split into their snake_case and
    camelCase parts, so a question can match them verbatim or paraphrased.

    Args:
        text: Text to tokenize.

    Returns:
        The list of tokens.
    """
    tokens: List[str] = []
    for word in re.findall(r"\w+", text):
        parts = split_identifier(word)
        tokens += [word] + (parts if len(parts) > 1 else [])
    words = [t.lower() for t in tokens if t.lower() not in STOPWORDS]
    return list(STEMMER.stemWords(words))


def read_file(path: str | Path) -> str:
    """Return the content of a UTF-8 text file.

    Args:
        path: File to read.

    Returns:
        The content, undecodable bytes being replaced.
    """
    with open(path, encoding="utf-8", errors="replace") as file:
        return file.read()


def warn(message: str) -> None:
    """Print a non-fatal problem on stderr.

    Args:
        message: Description of the problem.
    """
    print(f"Warning: {message}", file=sys.stderr)


def read_source(source: MinimalSource) -> str:
    """Return the text covered by a source.

    Args:
        source: File path and character range to read.

    Returns:
        The text of the range.
    """
    text = read_file(source.file_path)
    return text[source.first_character_index:source.last_character_index]


def build_context(sources: List[MinimalSource]) -> str:
    """Join the text of the sources that can be read.

    Args:
        sources: Retrieved sources, best first.

    Returns:
        The text of each source under its file name, empty if none is
        readable.
    """
    parts: List[str] = []
    for source in sources:
        try:
            parts.append(f"File: {source.file_path}\n{read_source(source)}")
        except OSError as error:
            warn(f"skipping source {source.file_path}: {error}")
    return "\n\n".join(parts)


def iou(a: MinimalSource, b: MinimalSource) -> float:
    """Compute the intersection over union of two sources.

    Args:
        a: First source.
        b: Second source.

    Returns:
        0 for different files, else the IoU of the character ranges.
    """
    if a.file_path != b.file_path:
        return 0.0
    inter = (min(a.last_character_index, b.last_character_index)
             - max(a.first_character_index, b.first_character_index))
    union = (max(a.last_character_index, b.last_character_index)
             - min(a.first_character_index, b.first_character_index))
    return max(inter, 0) / union if union > 0 else 0.0


def save(model: BaseModel, directory: str, name: str, label: str) -> None:
    """Write a pydantic model as JSON into a directory.

    Args:
        model: Data to write.
        directory: Output directory, created if needed.
        name: Output file name.
        label: Name of the data shown in the confirmation message.
    """
    path = Path(directory) / name
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as file:
        file.write(model.model_dump_json(indent=2))
    print(f"Saved {label} to {path}")


@RAW_TEXT
class RAG:
    """Command-line interface of the RAG system."""

    def __init__(self, raw_dir: str = "data/raw",
                 index_dir: str = "data/processed") -> None:
        """Set the corpus and index locations.

        Args:
            raw_dir: Directory of the corpus to index.
            index_dir: Directory where the index is stored.
        """
        self.raw_dir = raw_dir
        self.index_dir = index_dir
        self._retriever: Any = None
        self._tokenizer: Any = None
        self._llm: Any = None

    @RAW_TEXT
    def index(self, max_chunk_size: int = 2000,
              raw_dir: str = "data/raw") -> None:
        """Chunk the Python, Markdown and text files and build a BM25 index.

        Args:
            max_chunk_size: Maximum chunk length in characters (1 to 2000).
        """
        size = int(max_chunk_size)
        if not 1 <= size <= 2000:
            raise ValueError("max_chunk_size must be between 1 and 2000")
        python, text = (RecursiveCharacterTextSplitter.from_language(
            language, chunk_size=size, chunk_overlap=size // 10,
            add_start_index=True)
            for language in (Language.PYTHON, Language.MARKDOWN))
        files = sorted(p for p in Path(raw_dir).rglob("*")
                       if p.suffix in (".py", ".md", ".txt") and p.is_file())
        sources: List[dict[str, Any]] = []
        corpus: List[List[str]] = []
        for path in tqdm(files, desc="Indexing"):
            splitter = python if path.suffix == ".py" else text
            try:
                content = read_file(path)
            except OSError as error:
                warn(f"skipping {path}: {error}")
                continue
            for chunk in splitter.create_documents([content]):
                start = chunk.metadata["start_index"]
                sources.append(MinimalSource(
                    file_path=str(path), first_character_index=start,
                    last_character_index=start + len(chunk.page_content),
                ).model_dump())
                corpus.append(tokenize(f"{path} {chunk.page_content}"))
        if not corpus:
            raise FileNotFoundError(f"No file to index in {raw_dir}")
        retriever = bm25s.BM25()
        retriever.index(corpus)
        retriever.save(self.index_dir, corpus=sources)
        print(f"Ingestion complete! Indices saved under {self.index_dir}")

    def _search(self, question: UnansweredQuestion,
                k: int) -> MinimalSearchResults:
        """Retrieve the k best sources for a question.

        Args:
            question: The question to search for.
            k: Maximum number of sources to retrieve.

        Returns:
            The question with its sources, best first. Chunks scoring 0 are
            left out.
        """
        if self._retriever is None:
            self._retriever = bm25s.BM25.load(
                self.index_dir, load_corpus=True, show_progress=False)
        tokens = tokenize(question.question)
        scores = self._retriever.get_scores(tokens) if tokens else np.zeros(1)
        best = np.argsort(-scores)[:max(int(k), 0)]
        return MinimalSearchResults(
            question_id=question.question_id, question=question.question,
            retrieved_sources=[self._retriever.corpus[i]
                               for i in best if scores[i] > 0])

    def _generate(self, result: MinimalSearchResults) -> str:
        """Answer a question with Qwen from its retrieved sources.

        Args:
            result: The question and its retrieved sources.

        Returns:
            The generated answer, or a fixed message without running the
            model if no source can be read.
        """
        context = build_context(result.retrieved_sources)
        if not context:
            return "No relevant context was found to answer this question."
        if self._llm is None:
            self._tokenizer = AutoTokenizer.from_pretrained(MODEL)
            self._llm = AutoModelForCausalLM.from_pretrained(
                MODEL, dtype="float32")  # bfloat16 is very slow on CPU
        context = self._tokenizer.decode(
            self._tokenizer(context).input_ids[:CONTEXT_TOKENS])
        inputs = self._tokenizer.apply_chat_template(
            [{"role": "system", "content": PROMPT},
             {"role": "user",
              "content": f"Context:\n{context}\n\n"
                         f"Question: {result.question}"}],
            add_generation_prompt=True, enable_thinking=False,
            return_dict=True, return_tensors="pt")
        output = self._llm.generate(**inputs, max_new_tokens=512)
        answer: str = self._tokenizer.decode(
            output[0, inputs["input_ids"].shape[1]:], skip_special_tokens=True)
        return answer.strip()

    @RAW_TEXT
    def search(self, query: str, k: int = 10) -> None:
        """Print the top-k sources for a single query.

        Args:
            query: The question.
            k: Number of sources to retrieve.
        """
        count = max(int(k), 0)
        result = self._search(UnansweredQuestion(question=query), count)
        output = StudentSearchResults(search_results=[result], k=count)
        print(output.model_dump_json(indent=2))

    @RAW_TEXT
    def search_dataset(self, dataset_path: str,
                       save_directory: str = "data/output/search_results",
                       k: int = 10) -> None:
        """Search every question of a dataset and save the results.

        Args:
            dataset_path: JSON dataset of questions.
            save_directory: Directory where the results are written.
            k: Number of sources to retrieve per question.
        """
        count = max(int(k), 0)
        dataset = RagDataset.model_validate_json(read_file(dataset_path))
        results = [self._search(question, count) for question
                   in tqdm(dataset.rag_questions, desc="Searching")]
        save(StudentSearchResults(search_results=results, k=count),
             save_directory, Path(dataset_path).name, "student_search_results")

    @RAW_TEXT
    def answer(self, query: str, k: int = 10) -> None:
        """Print the answer to a single query with its sources.

        Args:
            query: The question.
            k: Number of sources to retrieve.
        """
        count = max(int(k), 0)
        result = self._search(UnansweredQuestion(question=query), count)
        answer = MinimalAnswer(**result.model_dump(),
                               answer=self._generate(result))
        output = StudentSearchResultsAndAnswer(search_results=[answer],
                                               k=count)
        print(output.model_dump_json(indent=2))

    @RAW_TEXT
    def answer_dataset(self, student_search_results_path: str,
                       save_directory: str =
                       "data/output/search_results_and_answer") -> None:
        """Answer every question of a search results file and save them.

        Args:
            student_search_results_path: JSON output of search_dataset.
            save_directory: Directory where the answers are written.
        """
        path = Path(student_search_results_path)
        results = StudentSearchResults.model_validate_json(read_file(path))
        print(f"Loaded {len(results.search_results)} questions")
        answers = [MinimalAnswer(**result.model_dump(),
                                 answer=self._generate(result))
                   for result in tqdm(results.search_results,
                                      desc="Answering")]
        save(StudentSearchResultsAndAnswer(search_results=answers,
                                           k=results.k),
             save_directory, path.name, "student_search_results_and_answer")

    @RAW_TEXT
    def evaluate(self, student_search_results_path: str,
                 dataset_path: str) -> None:
        """Print recall@k of search results against a ground-truth dataset.

        A reference source is found when a retrieved source of the same file
        overlaps it with an IoU of at least 0.05.

        Args:
            student_search_results_path: JSON output of search_dataset.
            dataset_path: JSON dataset of answered questions.
        """
        results = StudentSearchResults.model_validate_json(
            read_file(student_search_results_path))
        dataset = RagDataset.model_validate_json(read_file(dataset_path))
        retrieved = {r.question_id: r.retrieved_sources
                     for r in results.search_results}
        questions = [q for q in dataset.rag_questions
                     if isinstance(q, AnsweredQuestion) and q.sources]
        if not questions:
            raise ValueError("The dataset has no answered question")
        for k in (1, 3, 5, 10):
            recalls = [sum(any(iou(source, found) >= 0.05 for found
                               in retrieved.get(q.question_id, [])[:k])
                           for source in q.sources) / len(q.sources)
                       for q in questions]
            print(f"Recall@{k}: {sum(recalls) / len(recalls):.3f}")

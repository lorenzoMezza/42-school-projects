*This project has been created as part of the 42 curriculum by lmezzaba.*

# RAG against the machine

## Description

A Retrieval-Augmented Generation system that answers questions about the
vLLM 0.10.1 codebase. It indexes the repository, retrieves the snippets most
relevant to a question with BM25, and asks `Qwen/Qwen3-0.6B` to answer from
those snippets only. Retrieval quality is measured with recall@k.

## Instructions

Requirements: UV, Python 3.10 to 3.14 (UV downloads one if none is
installed) and about 2.5 GB of free disk: about 1.1 GB for the environment
(CPU-only PyTorch) and 1.4 GB for the model weights (downloaded from Hugging
Face on first use).

Expected layout: the vLLM repository in `data/raw/vllm-0.10.1/` and the
datasets in `data/datasets/{AnsweredQuestions,UnansweredQuestions}/`.

```bash
make install   # uv sync
make run       # uv run python -m src index (ARGS="..." runs another command)
make debug     # same command under pdb
make lint      # flake8 + mypy
make clean     # remove caches
```

Commands (`uv run python -m src <command>`):

| Command | Options |
|---------|---------|
| `index` | `--max_chunk_size 2000` |
| `search <query>` | `--k 10` |
| `search_dataset` | `--dataset_path`, `--save_directory data/output/search_results`, `--k 10` |
| `answer <query>` | `--k 10` |
| `answer_dataset` | `--student_search_results_path`, `--save_directory data/output/search_results_and_answer` |
| `evaluate` | `--student_search_results_path`, `--dataset_path` |

Every command also accepts `--raw_dir` (default `data/raw`) and `--index_dir`
(default `data/processed`). Search commands output a `StudentSearchResults`
JSON and answer commands a `StudentSearchResultsAndAnswer` JSON, printed for a
single query and written to a file for a dataset. Pass a `--save_directory`
scoped by dataset, since the public datasets share file names.

## Example usage

```bash
uv run python -m src index --max_chunk_size 2000
uv run python -m src search "How do I load a LoRA adapter at runtime?" --k 5
uv run python -m src answer "How do I load a LoRA adapter at runtime?" --k 5
uv run python -m src search_dataset \
    --dataset_path data/datasets/UnansweredQuestions/dataset_docs_public.json \
    --k 10 --save_directory data/output/search_results/UnansweredQuestions
uv run python -m src evaluate \
    --student_search_results_path data/output/search_results/UnansweredQuestions/dataset_docs_public.json \
    --dataset_path data/datasets/AnsweredQuestions/dataset_docs_public.json
uv run python -m src answer_dataset \
    --student_search_results_path data/output/search_results/UnansweredQuestions/dataset_docs_public.json \
    --save_directory data/output/search_results_and_answer/UnansweredQuestions
```

## Not enought memory problem fix

```
rm -rf ~/.cache/uv
export UV_CACHE_DIR=/goinfre/$USER/.uv-cache
export HF_HOME=/goinfre/$USER/.hf-cache
make
```

## System architecture

- `src/models.py`: the pydantic models exchanged between stages.
- `src/rag.py`: the pipeline, exposed as the methods of the `RAG` class.
  - **Indexing** (`index`): reads every `.py`, `.md` and `.txt` file of
    `data/raw/`, chunks it, tokenizes each chunk and saves a BM25 index plus
    the chunk locations (`file_path`, character range) in `data/processed/`.
  - **Retrieval** (`search`, `search_dataset`): tokenizes the question the same
    way, scores every chunk with BM25 and returns the k best locations.
  - **Augmentation and generation** (`answer`, `answer_dataset`): reads the text
    of the retrieved ranges from disk, truncates it to 4096 tokens, puts it in
    the prompt and lets Qwen3-0.6B (non-thinking mode) answer.
  - **Evaluation** (`evaluate`): recall@1/3/5/10, a reference source being
    found when a retrieved source of the same file has an IoU >= 0.05 with it.
- `src/__main__.py`: the Python Fire CLI; any error is printed as a short
  message instead of a traceback.

## Chunking strategy

Both strategies use LangChain's `RecursiveCharacterTextSplitter`, which splits
on the first separator of a list that yields pieces small enough, then merges
neighbouring pieces up to `max_chunk_size` characters (default 2000, never
more) with a 10% overlap. `max_chunk_size` must be between 1 and 2000. Very
small values are accepted but impractical, because the number of chunks
explodes: 50 characters give 580k chunks, 10 characters give 2.2M, and with
1 character the indexing ran out of memory on a 6 GB limit.

- **Python**: splits on top-level `class` and `def` boundaries first, then
  blank lines, lines and words, so a chunk tends to hold whole functions or
  classes.
- **Markdown / text**: splits on headings first, then code fences, horizontal
  rules, paragraphs, lines and words, so a chunk tends to hold a whole section.

The character offsets of each chunk in its file are kept, which is what the
search results report.

## Retrieval method

BM25 (Lucene variant, `k1=1.5`, `b=0.75`) through the `bm25s` library. The
tokenizer, shared by chunks and questions:

- keeps every identifier whole (`load_lora_adapter`) **and** adds its
  snake_case / camelCase parts (`load`, `lora`, `adapter`), so a question can
  match code that it quotes verbatim or describes in plain words;
- lowercases, drops English stopwords (the 179-word NLTK list shipped with
  `bm25s`, so question words like `how`, `what`, `do` do not match chat
  examples) and applies the Snowball stemmer.

The file path is prepended to each chunk before tokenization, so file and
directory names (`lora.md`, `fused_moe/`) count as evidence. Chunks are ranked
by score; chunks scoring 0 are never returned, so a nonsensical query gets no
sources instead of random ones.

## Performance analysis

Recall measured on the public datasets with the provided moulinette (my
`evaluate` command gives the same numbers):

| `max_chunk_size` | Dataset | R@1 | R@3 | R@5 | R@10 |
|------|------|------|------|------|------|
| 2000 | docs | 0.66 | 0.82 | **0.89** | 0.93 |
| 2000 | code | 0.55 | 0.76 | **0.84** | 0.88 |
| 1000 | docs | 0.64 | 0.84 | 0.90 | 0.93 |
| 1000 | code | 0.53 | 0.79 | 0.81 | 0.89 |
| 500 | docs | 0.59 | 0.82 | 0.84 | 0.90 |
| 500 | code | 0.55 | 0.74 | 0.82 | 0.91 |

Smaller chunks barely change recall@5: they are more precise, but each one
holds fewer of the question's words. 2000 gives the most context to the model.

Effect of the tokenizer choices (recall@5, chunk size 2000):

| Variant | docs | code |
|---------|------|------|
| final tokenizer | 0.89 | 0.84 |
| without the file path in the chunk | 0.84 | 0.71 |
| without identifier splitting | 0.86 | 0.63 |
| without stemming | 0.87 | 0.80 |
| 33-word Lucene stopword list | 0.84 | 0.83 |

Speed on a laptop CPU: indexing the corpus (about 2000 files, 15000 chunks)
takes under 10 seconds, searching 100 questions about 2 seconds (limits: 5
minutes and 90 seconds for 200 questions). Answer generation takes 10 to 20
seconds per question on CPU.

## Design decisions

- **CPU-only PyTorch** (`[tool.uv.sources]` in `pyproject.toml`): the
  evaluation machines have no GPU, and the default Linux wheels add about
  4.5 GB of CUDA libraries (environment of 5.5 GB instead of about 1 GB).
  Python is capped below 3.15 because PyTorch has no wheels for it yet.
- **BM25 over TF-IDF**: term frequency saturation and length normalisation
  suit chunks of very different sizes.
- **Libraries for the generic parts** (`bm25s`, LangChain splitters,
  `transformers`) so the code only holds the project-specific logic.
- **Locations, not text, in the index**: the index stores where a chunk is;
  its text is read back from the corpus when answering, which is also what
  `answer_dataset` needs since it only receives search results.
- **Grounding prompt**: the model is told to answer from the context only and
  to say when it is not enough; Qwen3's thinking mode is disabled to keep
  answers short and fast. Without any retrieved source, the model is not run.

## Challenges faced

- **Questions paraphrase code**: plain word tokens left most code questions
  unmatched (`fused_batched_moe` vs "fused batched MoE"). Splitting
  identifiers while keeping them whole fixed it.
- **Conversational questions**: with the 33-word Lucene stopword list, `how`,
  `do`, `what` stayed in the query and pulled chat examples to the top
  ("How do I enable prefix caching?" returned tool-calling demos). The NLTK
  list fixed it and raised docs recall@5 from 0.84 to 0.89.
- **Right file, wrong chunk**: just over half of the misses at recall@5 on the
  public datasets (15 of 27) point to another part of the right file, the
  others to another file. The chunk overlap and the file path tokens helped;
  the rest needs semantic retrieval.
- **Slow generation**: the model loads in bfloat16 by default, which took
  about 3 minutes per question on CPU. Loading it in float32 brought that down
  to 10 to 20 seconds with the same answers.
- **Degenerate inputs**: empty or unknown-word queries, `k <= 0`, missing files
  and malformed JSON all end in a clean message, never a traceback. A corpus
  file or a retrieved source that cannot be read is skipped with a warning, so
  it does not stop a whole indexing or `answer_dataset` run.
- **Fire parses arguments as Python literals**: a query like `"hello, world"`
  became the tuple `('hello', 'world')`. Every command now receives its
  arguments as plain strings (`fire.decorators.SetParseFn(str)`) and converts
  the numeric ones itself.

## Resources

- Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP
  Tasks* (2020): https://arxiv.org/abs/2005.11401
- Robertson & Zaragoza, *The Probabilistic Relevance Framework: BM25 and
  Beyond* (2009)
- bm25s: https://github.com/xhluca/bm25s
- LangChain text splitters: https://python.langchain.com/docs/concepts/text_splitters/
- Qwen3 model card: https://huggingface.co/Qwen/Qwen3-0.6B
- Python Fire: https://github.com/google/python-fire

**AI usage**: an AI assistant was used to understand the subject, draft this README,
and run the recall experiments (chunk size,
tokenizer ablations).
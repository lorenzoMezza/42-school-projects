"""Entry point: uv run python -m src <command> [options]."""
import sys

import fire

from .rag import RAG


def main() -> None:
    """Run the Fire CLI, reporting any error without a traceback."""
    try:
        fire.Fire(RAG)
    except (Exception, KeyboardInterrupt) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

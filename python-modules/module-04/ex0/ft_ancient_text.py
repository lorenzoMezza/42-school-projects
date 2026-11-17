import sys
import typing


def print_block(content: str) -> None:
    print("---")
    print(content, end="")
    if len(content) > 0 and content[-1] != "\n":
        print()
    print("---")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    path = sys.argv[1]
    file: typing.IO[str]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{path}'")

    try:
        file = open(path, "r")
        content = file.read()
        file.close()
    except OSError as error:
        print(f"Error opening file '{path}': {error}")
        return

    print_block(content)
    print(f"File '{path}' closed.")


if __name__ == "__main__":
    main()

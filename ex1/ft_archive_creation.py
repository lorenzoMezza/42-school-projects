import sys
import typing


def print_block(content: str) -> None:
    print("---")
    print(content, end="")
    if len(content) > 0 and content[-1] != "\n":
        print()
    print("---")


def add_archive_char(content: str) -> str:
    new_content = ""
    index = 0

    while index < len(content):
        if content[index] == "\n":
            new_content += "#\n"
        else:
            new_content += content[index]
        index += 1

    if len(content) > 0 and content[-1] != "\n":
        new_content += "#"

    return new_content


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    path = sys.argv[1]
    file: typing.IO[str]
    output_file: typing.IO[str]

    print("=== Cyber Archives Recovery & Preservation ===")
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

    new_content = add_archive_char(content)

    print("Transform data:")
    print_block(new_content)

    save_path = input("Enter new file name (or empty): ")

    if save_path == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{save_path}'")

    try:
        output_file = open(save_path, "w")
        output_file.write(new_content)
        output_file.close()
        print(f"Data saved in file '{save_path}'.")
    except OSError as error:
        print(f"Error opening file '{save_path}': {error}")
        print("Data not saved.")


if __name__ == "__main__":
    main()

def secure_archive(
    file_name: str,
    action: str = "read",
    content: str = "",
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(file_name, "r") as file:
                return (True, file.read())
        if action == "write":
            with open(file_name, "w") as file:
                file.write(content)
            return (True, "Content successfully written to file")
        return (False, "Invalid action")
    except OSError as error:
        return (False, str(error))


def get_inaccessible_file() -> str:
    test_paths = ("/etc/master.passwd", "/etc/shadow")

    for path in test_paths:
        result = secure_archive(path)
        if not result[0] and "Permission denied" in result[1]:
            return path
    return "/etc/master.passwd"


def main() -> None:
    sample_content = (
        "[FRAGMENT 001] Digital preservation protocols established 2087\n"
        "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
        "[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
    )

    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive(get_inaccessible_file()))

    secure_archive("ancient_fragment.txt", "write", sample_content)

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)

    print("Using 'secure_archive' to write previous content to a new file:")
    if result[0]:
        print(secure_archive("new_fragment.txt", "write", result[1]))
    else:
        print((False, "No content available to write"))


if __name__ == "__main__":
    main()

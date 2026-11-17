import os
import site
import sys


def is_virtual_environment() -> bool:
    return sys.prefix != sys.base_prefix or hasattr(sys, "real_prefix")


def get_environment_name(path: str) -> str:
    name = os.path.basename(path)
    if name == "":
        return path
    return name


def get_package_paths() -> list[str]:
    try:
        paths = site.getsitepackages()
    except AttributeError:
        paths = []

    if len(paths) == 0:
        paths.append(site.getusersitepackages())

    return paths


def print_package_paths() -> None:
    paths = get_package_paths()
    print("Package installation path:")
    for path in paths:
        print(path)


def print_activation_instructions() -> None:
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print(r"matrix_env\Scripts\activate  # On Windows")
    print("Then run this program again.")


def print_global_status() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print(f"Global Environment Path: {sys.base_prefix}")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print_package_paths()
    print_activation_instructions()


def print_virtual_status() -> None:
    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {get_environment_name(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}")
    print(f"Global Python Path: {sys.base_prefix}")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print_package_paths()


def main() -> int:
    if is_virtual_environment():
        print_virtual_status()
    else:
        print_global_status()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
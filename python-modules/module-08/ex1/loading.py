import importlib
import importlib.metadata
import sys


REQUIRED_PACKAGES: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}

OUTPUT_FILE = "matrix_analysis.png"
DATA_POINTS = 1000


def get_package_version(package_name: str) -> str:
    try:
        return importlib.metadata.version(package_name)
    except importlib.metadata.PackageNotFoundError:
        return "not installed"


def print_installation_help(missing_packages: list[str]) -> None:
    print()
    print("Missing dependencies detected:")
    for package_name in missing_packages:
        print(f"[MISSING] {package_name}")
    print()
    print("Install them with pip:")
    print("pip install -r requirements.txt")
    print()
    print("Or install them with Poetry:")
    print("poetry install")
    print("poetry run python loading.py")


def check_dependencies() -> bool:
    missing_packages: list[str] = []

    print("Checking dependencies:")
    for package_name, message in REQUIRED_PACKAGES.items():
        try:
            importlib.import_module(package_name)
            version = get_package_version(package_name)
            print(f"[OK] {package_name} ({version}) - {message}")
        except ImportError:
            missing_packages.append(package_name)
            print(f"[MISSING] {package_name} - {message}")

    if missing_packages:
        print_installation_help(missing_packages)
        return False
    return True


def print_dependency_management_comparison() -> None:
    print()
    print("Dependency management comparison:")
    print("pip:")
    print("  - Uses requirements.txt")
    print("  - Installs packages into the current environment")
    print("  - Simple and direct, but mostly manual")
    print("Poetry:")
    print("  - Uses pyproject.toml")
    print("  - Creates or manages a virtual environment")
    print("  - Can create poetry.lock for reproducible installs")
    print()
    print("Installed package versions:")
    for package_name in REQUIRED_PACKAGES:
        version = get_package_version(package_name)
        print(f"  - {package_name}: {version}")
    print()


def run_analysis() -> None:
    import matplotlib

    matplotlib.use("Agg")

    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    print("Analyzing Matrix data...")

    random_generator = np.random.default_rng(seed=42)
    cycles = np.arange(DATA_POINTS)
    signal = random_generator.normal(50, 10, DATA_POINTS)
    anomaly = random_generator.integers(0, 100, DATA_POINTS)

    data_frame = pd.DataFrame(
        {
            "cycle": cycles,
            "signal": signal,
            "anomaly": anomaly,
        }
    )
    data_frame["system_load"] = (
        data_frame["signal"] + data_frame["anomaly"] * 0.25
    )

    print(f"Processing {len(data_frame)} data points...")
    print(f"Average signal: {data_frame['signal'].mean():.2f}")
    print(f"Max anomaly: {data_frame['anomaly'].max()}")

    print("Generating visualization...")
    plt.plot(
        data_frame["cycle"].to_numpy(),
        data_frame["system_load"].to_numpy(),
    )
    plt.title("Matrix Data Analysis")
    plt.xlabel("Cycle")
    plt.ylabel("System load")
    plt.tight_layout()
    plt.savefig(OUTPUT_FILE)
    plt.close()

    print("Analysis complete!")
    print(f"Results saved to: {OUTPUT_FILE}")


def main() -> int:
    print("LOADING STATUS: Loading programs...")
    if not check_dependencies():
        return 1
    print_dependency_management_comparison()
    run_analysis()
    return 0


if __name__ == "__main__":
    sys.exit(main())

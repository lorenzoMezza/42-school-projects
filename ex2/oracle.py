import os
import sys


VALID_MODES = ("development", "production")
VALID_LOG_LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")
REQUIRED_KEYS = ("DATABASE_URL", "API_KEY", "ZION_ENDPOINT")
DEVELOPMENT_DATABASE = "sqlite:///matrix_dev.db"
DEVELOPMENT_ZION = "http://localhost:8080/zion"


class MatrixConfig:
    """Store the Matrix configuration loaded from the environment."""

    def __init__(
        self,
        mode: str,
        database_url: str,
        api_key: str,
        log_level: str,
        zion_endpoint: str,
        warnings: list[str],
        errors: list[str],
        env_file_loaded: bool,
    ) -> None:
        self.mode = mode
        self.database_url = database_url
        self.api_key = api_key
        self.log_level = log_level
        self.zion_endpoint = zion_endpoint
        self.warnings = warnings
        self.errors = errors
        self.env_file_loaded = env_file_loaded


class DotenvStatus:
    """Store the result of loading the .env file."""

    def __init__(self, loaded: bool, missing_dependency: bool) -> None:
        self.loaded = loaded
        self.missing_dependency = missing_dependency


def get_project_file(filename: str) -> str:
    """Return an absolute path for a file stored next to this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)


def print_missing_dotenv_dependency() -> None:
    """Print installation help when python-dotenv is not installed."""
    print("ORACLE STATUS: Unable to read the Matrix")
    print("Missing dependency: python-dotenv")
    print("Install it with:")
    print("python3 -m pip install python-dotenv")


def load_environment_file() -> DotenvStatus:
    """Load variables from .env without overriding real environment values."""
    try:
        from dotenv import load_dotenv
    except ModuleNotFoundError:
        return DotenvStatus(False, True)

    env_path = get_project_file(".env")
    loaded = load_dotenv(env_path, override=False)
    return DotenvStatus(loaded, False)


def get_env_value(name: str) -> str:
    """Return a clean environment variable value, or an empty string."""
    value = os.environ.get(name, "")
    return value.strip()


def is_placeholder_secret(value: str) -> bool:
    """Return True when a secret looks like a sample or placeholder value."""
    lowered = value.lower()
    placeholders = (
        "",
        "change_me",
        "changeme",
        "replace_me",
        "replace-with-your-api-key",
        "your-api-key-here",
        "demo",
        "secret123",
    )
    return lowered in placeholders


def normalize_mode(raw_mode: str, warnings: list[str]) -> str:
    """Return a valid Matrix mode, defaulting safely to development."""
    if raw_mode == "":
        warnings.append("MATRIX_MODE missing; using development mode.")
        return "development"
    mode = raw_mode.lower()
    if mode not in VALID_MODES:
        warnings.append(
            "MATRIX_MODE must be development or production; "
            "using development mode."
        )
        return "development"
    return mode


def normalize_log_level(raw_level: str, mode: str, warnings: list[str]) -> str:
    """Return a valid log level for the active mode."""
    if raw_level == "":
        if mode == "development":
            return "DEBUG"
        return "WARNING"
    level = raw_level.upper()
    if level not in VALID_LOG_LEVELS:
        warnings.append("LOG_LEVEL invalid; using INFO.")
        return "INFO"
    return level


def build_config(dotenv_status: DotenvStatus) -> MatrixConfig:
    """Build a validated configuration object from environment variables."""
    warnings: list[str] = []
    errors: list[str] = []

    if not dotenv_status.loaded:
        warnings.append(
            ".env file not found or empty; using environment/defaults."
        )

    mode = normalize_mode(get_env_value("MATRIX_MODE"), warnings)
    log_level = normalize_log_level(get_env_value("LOG_LEVEL"), mode, warnings)
    database_url = get_env_value("DATABASE_URL")
    api_key = get_env_value("API_KEY")
    zion_endpoint = get_env_value("ZION_ENDPOINT")

    if database_url == "" and mode == "development":
        database_url = DEVELOPMENT_DATABASE
        warnings.append(
            "DATABASE_URL missing; using local development database."
        )
    if zion_endpoint == "" and mode == "development":
        zion_endpoint = DEVELOPMENT_ZION
        warnings.append(
            "ZION_ENDPOINT missing; using local development endpoint."
        )

    if mode == "production":
        for key in REQUIRED_KEYS:
            if get_env_value(key) == "":
                errors.append(f"{key} is required in production mode.")
        if log_level == "DEBUG":
            warnings.append("DEBUG logging is unsafe in production.")
        if api_key.startswith("dev-") or is_placeholder_secret(api_key):
            errors.append("API_KEY must be a real production secret.")
    elif api_key == "":
        warnings.append("API_KEY missing; external API access is disabled.")

    return MatrixConfig(
        mode,
        database_url,
        api_key,
        log_level,
        zion_endpoint,
        warnings,
        errors,
        dotenv_status.loaded,
    )


def describe_database(config: MatrixConfig) -> str:
    """Return a safe database status message."""
    if config.database_url == "":
        return "Missing configuration"
    if config.database_url.startswith("sqlite"):
        return "Connected to local instance"
    return "Configured for remote storage"


def describe_api_access(config: MatrixConfig) -> str:
    """Return a safe API status without printing the secret."""
    if config.api_key == "":
        return "Missing"
    if is_placeholder_secret(config.api_key):
        return "Placeholder configured"
    return "Authenticated"


def describe_zion(config: MatrixConfig) -> str:
    """Return the Zion network status."""
    if config.zion_endpoint == "":
        return "Offline"
    return "Online"


def print_runtime_profile(config: MatrixConfig) -> None:
    """Show a visible difference between development and production."""
    if config.mode == "development":
        print("Runtime Profile: development sandbox")
        print("Policy: local services and DEBUG logging are allowed")
    else:
        print("Runtime Profile: production mainframe")
        print("Policy: strict secrets and remote services are required")


def gitignore_protects_env() -> bool:
    """Return True when .gitignore contains a rule for .env."""
    gitignore_path = get_project_file(".gitignore")
    try:
        with open(gitignore_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except OSError:
        return False

    cleaned_lines = []
    for line in lines:
        clean_line = line.strip()
        if clean_line != "" and not clean_line.startswith("#"):
            cleaned_lines.append(clean_line)
    return ".env" in cleaned_lines or ".env*" in cleaned_lines


def example_file_exists() -> bool:
    """Return True when the safe template file exists."""
    return os.path.isfile(get_project_file(".env.example"))


def print_security_check(config: MatrixConfig) -> None:
    """Print security checks related to secret management."""
    print("Environment security check:")
    print("[OK] Configuration is loaded from environment variables")
    if gitignore_protects_env():
        print("[OK] .env file is protected by .gitignore")
    else:
        print("[WARN] .gitignore should contain .env")
    if example_file_exists():
        print("[OK] .env.example template is available")
    else:
        print("[WARN] .env.example template is missing")
    if config.mode == "production" and len(config.errors) == 0:
        print("[OK] Production overrides available")
    elif config.mode == "development":
        print(
            "[OK] Production overrides available through "
            "environment variables"
        )


def print_configuration(config: MatrixConfig) -> None:
    """Print the loaded configuration without leaking secrets."""
    print("Configuration loaded:")
    print(f"Mode: {config.mode}")
    print(f"Database: {describe_database(config)}")
    print(f"API Access: {describe_api_access(config)}")
    print(f"Log Level: {config.log_level}")
    print(f"Zion Network: {describe_zion(config)}")
    print_runtime_profile(config)


def print_diagnostics(config: MatrixConfig) -> None:
    """Print warnings and errors collected during configuration loading."""
    if len(config.warnings) > 0:
        print("Warnings:")
        for warning in config.warnings:
            print(f"[WARN] {warning}")
    if len(config.errors) > 0:
        print("Errors:")
        for error in config.errors:
            print(f"[ERROR] {error}")


def main() -> int:
    """Load and display the Oracle configuration."""
    print("ORACLE STATUS: Reading the Matrix...")
    dotenv_status = load_environment_file()
    if dotenv_status.missing_dependency:
        print_missing_dotenv_dependency()
        return 1

    config = build_config(dotenv_status)
    print_configuration(config)
    print_security_check(config)
    print_diagnostics(config)
    if len(config.errors) > 0:
        print("The Oracle refuses unsafe production configuration.")
        return 1
    print("The Oracle sees all configurations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

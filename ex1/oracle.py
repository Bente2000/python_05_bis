import os
import sys
from dotenv import load_dotenv # sets variables from .env in os.environ
from dotenv import dotenv_values


KEYS:tuple[str, ...] = ("MATRIX_MODE",
                        "DATABASE_URL",
                        "API_KEY",
                        "LOG_LEVEL",
                        "ZION_ENDPOINT")


class SecurityError(Exception):
    pass


def load_config() -> dict[str, str | None]: # loads conifg from environment variables
    load_dotenv(override=False) # werkt
    config: dict[str, str | None] = {key: os.getenv(key) for key in KEYS} # key:value
    print(config)
    missing: list[str] = [key for key, value in config.items() if not value]
    if missing:
        print(f"Configuration missing: {missing}")
    return config


def gitignore_check() -> None:
    with open("ex1/.gitignore") as gitignore:
        arguments = [line.strip() for line in gitignore]
        if ".env" not in arguments:
            raise SecurityError("'.env' not present in gitignore.")


def secret_check(config: dict[str, str | None]) -> None:
    secrets: dict[str, str] = {}
    with open(__file__) as this_file:
        read = this_file.read()
    if config["API_KEY"] is not None:
        secrets["API_KEY"] = config["API_KEY"]
    if config["DATABASE_URL"] is not None:
        secrets["DATABASE_URL"] = config["DATABASE_URL"]
    for secret in secrets:
        if secret in read:
            raise SecurityError("Hardcoded secrets detected")


def print_config(config: dict[str, str | None]) -> None:
    print(f"Mode: {config['MATRIX_MODE'] or "development"}")
    if config["MATRIX_MODE"] == "production":
        config["LOG_LEVEL"] = "minimal"
        config["DATABASE_URL"] = "production"
    else:
        config["LOG_LEVEL"] = "verbose"
        config["DATABASE_URL"] = "local"
    print(f"Database: connected to {config['DATABASE_URL']} database")
    print("API Access: " + ("Authenticated" if config["API_KEY"] else "Not "
    "authenticated"))
    print(f"Log level: {config['LOG_LEVEL']}")
    print("Remote network: " + ("Online" if config["ZION_ENDPOINT"] else
    "Offline"))


if __name__ == "__main__":
    print("\nORACLE STATUS: Consulting the configuration...\n")
    config: dict[str, str | None] = load_config()
    print("Configuration loaded:")
    print_config(config)
    print("\nConfiguration security check:")
    try:
        gitignore_check()
        print("[OK] .env file properly ignored by git")
    except OSError:
        print("[FAIL] No .gitignore file present")
    except SecurityError as e:
        print(f"[FAIL] {e}")
    try:
        secret_check(config)
        print("[OK] No hardcoded secrets detected")
    except OSError:
        print("Filed to read this file")
    except SecurityError as e:
        print(f"[FAIL] {e}")
    print("[OK] Production overrides available\n")
    print("\nThe Oracle sees all configurations.")

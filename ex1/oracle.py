import os
import sys
from dotenv import load_dotenv # sets variables from .env in os.environ
from dotenv import dotenv_values

KEYS:tuple[str, ...] = ("MATRIX_MODE",
                        "DATABASE_URL",
                        "API_KEY",
                        "LOG_LEVEL",
                        "ZION_ENDPOINT")

class ConfigError(Exception):
    pass

def load_config() -> None: # loads conifg from environment variables
    raw_config: dict[str, str | None] = {}
    missing: list[str] = []
    load_dotenv(override=False) # werkt
    MATRIX_MODE = os.getenv("MATRIX_MODE")
    print(MATRIX_MODE)
    raw_config = {key: os.getenv(key) for key in KEYS} # key:value
    print(raw_config)
    missing = [key for key, value in raw_config.items() if not value]
    if missing:
        print(f"Keys missing from config: {missing}")


def security_check() -> None:
    try:
        with open("ex1/.gitignore") as gitignore:
            gitignore.read().split()
#            if ".env" and ".env\n" not in gitignore:
#                raise ConfigError("'.env' not present in .gitignore")
    except OSError:
        print("No .gitignore file present")
        sys.exit()
    except ConfigError as e:
        print(e)
        sys.exit()

if __name__ == "__main__":
    print("\nORACLE STATUS: Consulting the configuration...\n")
    security_check()
    load_config()

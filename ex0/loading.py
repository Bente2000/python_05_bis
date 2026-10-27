import importlib

reagents: dict[str, str] = {"pandas":"Data manipulation ready",
                            "numpy":"Numerical computation ready"}


def check_dependencies() -> None:
    missing: list[str] = []
    for name, message in reagents.items():
        try:
            module = importlib.import_module(name)
        except ImportError as e:
            print(f"[MISSING] {name} - not installed {e}")
            missing.append(name)
            continue
        version = getattr(module, "__version__", "version unknown")
        print(f"[OK] {name} ({version}) - {message}")

    if missing:
        print("\nMissing reagents, install them with pip or Poetry:\n"
              "pip:\n  pip install -r requirements.txt\n" # -r: look in file
              "Poetry:\n  poetry install\n  poetry run python loading.py")
        # run from poetry environment
    else:
        print("All reagents are installed")


if __name__ == "__main__":
    print("REAGENT STATUS: Loading reagents...\n\nChecking dependencies:")
    check_dependencies()
    print("\npip vs Poetry\n"
          "requirements.txt declares what to install; pip resolves it at"
          " install time.\n"
          "pyproject.toml declares the same constraints, Poetry pins the "
          "resolved versions in poetry.lock so every install is identical.")


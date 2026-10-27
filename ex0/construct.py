import os
import sys
import site


def not_in_venv() -> None:
    print("LABORATORY STATUS: You are working in the open\n"
          f"Current Python: {sys.executable}\n"
          "Virtual Environment: None detected\n\n"
          "WARNING: You are in the global environment!\n"
          "Every reagent you install here leaks into the whole system.\n\n"
          "To seal the laboratory, run:\n"
          "python3 -m venv lab_venv\n" # -m = run module as script
          "source lab_env/bin/activate\n\n"
          "Then run this program again.")


def in_venv() -> None:
    print("LABORATORY STATUS: The laboratory is sealed\n\n" 
          f"Current Python: {sys.executable}\n"
          f"Virtual Environment: {os.path.basename(sys.prefix)}\n"
          f"Environment path: {sys.prefix}\n\n"
          "SUCCESS: You are working in an isolated environment!\n"
          "Safe to install reagents without affecting the global system.\n\n"
          "Reagent installation path:\n"
          f"{site.getsitepackages()[0]}")


def venv_check() -> None:
    if sys.prefix == sys.base_prefix:
        not_in_venv()
    else:
        in_venv() # sys.prefix == venv


if __name__ == "__main__":
    venv_check()

# venv isolates just packages (OS and files stay the same), which go in
# site-packages folder

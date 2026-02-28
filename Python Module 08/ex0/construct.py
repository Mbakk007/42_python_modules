import sys


def in_virtualenv() -> bool:
    # sys.prefix points to active environment
    # sys.base_prefix points to global Python install
    # If they differ → running inside virtualenv
    return sys.prefix != sys.base_prefix


if __name__ == "__main__":
    if in_virtualenv():
        print("MATRIX STATUS: Welcome to the construct\n")
        print("Current Python:", sys.executable)
        print("Virtual Environment: ", sys.prefix.split("/")[-1])
        print("Environment Path:", sys.prefix)
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")
        print("Package installation path:")
        print(sys.prefix + "/lib/python3.11/site-packages")
    else:
        print("MATRIX STATUS: You're still plugged in\n")
        print("Current Python:", sys.executable)
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:\npython -m venv matrix_env")
        print("\nsource matrix_env/bin/activate # On Unix\nmatrix_env")
        print("\nScripts\nactivate # On Windows")
        print("Then run this program again.")

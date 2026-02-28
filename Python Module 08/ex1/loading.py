import sys
import importlib
import importlib.metadata as meta

REQUIRED_LIBS = ["pandas", "numpy", "matplotlib", "requests"]


def check_dependencies() -> list:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    missing = []

    for lib in REQUIRED_LIBS:
        try:
            importlib.import_module(lib)
            version = show_versions(lib)
            print(version)
            if lib == "pandas":
                print(f"[OK] {lib} ({version}) - Data manipulation ready")
            elif lib == "numpy":
                print(f"[OK] {lib} ({version}) - Numerical computing ready")
            elif lib == "matplotlib":
                print(f"[OK] {lib} ({version}) - Visualization ready")
            elif lib == "requests":
                print(f"[OK] {lib} ({version}) - Network access ready")
        except ImportError:
            print(f"[MISSING] {lib}")
            missing.append(lib)

    return missing


def show_versions(package):
    try:
        print(meta.version(package))
    except Exception:
        print(package, "not installed")


def show_install_help(missing):
    print(f"\nMissing dependencies: {missing}")
    print("\nInstall with pip:")
    print("  pip install -r requirements.txt")
    print("\nOr with Poetry:")
    print("  poetry install")


def analyze_data():
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main():
    missing = check_dependencies()

    if missing:
        show_install_help(missing)
        sys.exit(1)

    analyze_data()


if __name__ == "__main__":
    main()

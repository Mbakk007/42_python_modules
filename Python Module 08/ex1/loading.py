import sys
import importlib
import importlib.metadata as meta

REQUIRED_LIBS = ["pandas", "numpy", "matplotlib"]


def check_dependencies() -> list:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    missing = []

    for lib in REQUIRED_LIBS:
        try:
            importlib.import_module(lib)
            version = show_versions(lib)
            if lib == "pandas":
                print(f"[OK] {lib} ({version}) - Data manipulation ready")
            elif lib == "numpy":
                print(f"[OK] {lib} ({version}) - Numerical computing ready")
            elif lib == "matplotlib":
                print(f"[OK] {lib} ({version}) - Visualization ready")
        except ImportError:
            print(f"[MISSING] {lib}")
            missing.append(lib)

    return missing


def show_versions(package):
    try:
        return meta.version(package)
    except Exception:
        print(package, "not installed")


def show_install_help(missing):
    print(f"\nMissing dependencies: {missing}")
    print("\nInstall with pip:")
    print("  pip install -r requirements.txt")
    print("\nOr with Poetry:")
    print("  poetry install")


def analyze_data():
    print("\nAnalyzing Matrix data...")

    import numpy
    import pandas
    import matplotlib.pyplot

    data_points = 1000
    print(f"Processing {data_points} data points...")

    numpy.random.seed(42)
    signal = numpy.random.randint(0, 100, size=data_points)

    df = pandas.DataFrame({"signal": signal})
    print("Generating visualization...")

    matplotlib.pyplot.plot(df["signal"])
    matplotlib.pyplot.savefig("matrix_analysis.png")
    matplotlib.pyplot.close()

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main():
    missing = check_dependencies()

    if missing:
        show_install_help(missing)
        sys.exit(1)

    analyze_data()


if __name__ == "__main__":
    main()

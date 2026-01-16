def garden_operations() -> None:
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as r:
        print(f"Caught ValueError: {r}")
    print("Testing ZeroDivisionError...")
    try:
        20 / 0
    except ZeroDivisionError as r:
        print(f"Caught ZeroDivisionError: {r}")
    print("Testing FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError as r:
        print(f"Caught FileNotFoundError: {r}")
    print("Testing KeyError...")
    try:
        dictionary = {"42": 6, "Malaga": 15}
        print(dictionary["test"])
    except KeyError as r:
        print(f"Caught KeyError: {r}")
        return None


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    garden_operations()

    print("Testing multiple errors together...")
    try:
        value = int("not_a_number")
        value / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()

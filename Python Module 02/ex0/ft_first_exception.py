def check_temperature(temp_str: str) -> int | None:
    try:
        temperature = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None

    if temperature < 0:
        print(f"Error: {temperature}°C is too cold for plants (min 0°C)")
        return None

    if temperature > 40:
        print(f"Error: {temperature}°C is too hot for plants (max 40°C)")
        return None

    return temperature


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")

    test_values = ["25", "abc", "100", "-50"]

    for value in test_values:
        print(f"Testing temperature: {value}")
        result = check_temperature(value)

        if result is not None:
            print(f"Temperature {result}°C is perfect for plants!")

    print("All tests completed - program didn't crash!")

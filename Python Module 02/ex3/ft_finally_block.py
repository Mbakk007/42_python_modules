def water_plants(plant_list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if not plant:
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as error:
        print(f"Error: {error}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    print("Testing normal watering...")
    plants1 = ["tomato", "lettuce", "carrots"]
    water_plants(plants1)
    print("Watering completed successfully!")

    print("Testing with error...")
    plants2 = ["tomato", None, "carrots"]
    water_plants(plants2)
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()

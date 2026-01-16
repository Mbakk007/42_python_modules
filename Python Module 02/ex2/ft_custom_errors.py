class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant_health() -> None:
    raise PlantError("The tomato plant is wilting!")


def check_water_supply() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        check_plant_health()
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print("Testing WaterError...")
    try:
        check_water_supply()
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print("Testing catching all garden errors...")
    for action in (check_plant_health, check_water_supply):
        try:
            action()
        except GardenError as error:
            print(f"Caught a garden error: {error}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()

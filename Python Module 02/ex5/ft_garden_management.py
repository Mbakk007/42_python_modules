class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = {}  # plant_name -> {"water": int, "sun": int}

    def add_plant(self, plant_name: str, water_level: int,
                  sunlight_hours: int) -> None:
        try:
            if not plant_name:
                raise PlantError("Plant name cannot be empty!")
            if not (1 <= water_level <= 10):
                raise PlantError(f"Water level {water_level}"
                                 f" is out of range (1-10)")
            if not (2 <= sunlight_hours <= 12):
                raise PlantError(f"Sunlight hours {sunlight_hours}"
                                 f" is out of range (2-12)")
            self.plants[plant_name] = {"water": water_level,
                                       "sun": sunlight_hours}
            print(f"Added {plant_name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant, info in self.plants.items():
                if info["water"] < 1:
                    raise WaterError("Not enough water in tank")
                info["water"] += 1
                print(f"Watering {plant} - success")
        except WaterError as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        print("Checking plant health...")
        for plant, info in self.plants.items():
            try:
                if not plant:
                    raise PlantError("Plant name cannot be empty!")
                if not (1 <= info["water"] <= 10):
                    raise PlantError(f"Water level {info['water']}"
                                     f" is too high (max 10)")
                if not (2 <= info["sun"] <= 12):
                    raise PlantError(f"Sunlight hours {info['sun']}"
                                     f" is out of range (2-12)")
                print(f"{plant}: healthy (water: {info['water']},"
                      f" sun: {info['sun']})")
            except PlantError as e:
                print(f"Error checking {plant}: {e}")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    garden = GardenManager()

    print("Adding plants to garden...")
    garden.add_plant("tomato", 5, 8)
    garden.add_plant("lettuce", 15, 8)
    garden.add_plant("", 5, 6)

    print("Watering plants...")
    garden.water_plants()

    garden.check_plant_health()

    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()

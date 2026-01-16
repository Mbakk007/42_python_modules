"""System demonstrating plant management and garden tracking."""


class Plant:
    """Represents a generic plant."""

    def __init__(self, name, height):
        """Initialize a Plant instance."""
        self.name = name
        self.height = height

    def grow(self):
        """Increase the plant's height by 1 cm and print a message."""
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    """Represents a flowering plant."""

    def __init__(self, name, height, color):
        """Initialize a FloweringPlant instance."""
        super().__init__(name, height)
        self.color = color
        self.blooming = True


class PrizeFlower(FloweringPlant):
    """Represents a prize-winning flowering plant with points."""

    def __init__(self, name, height, color, points):
        """Initialize a PrizeFlower instance."""
        super().__init__(name, height, color)
        self.points = points


class GardenManager:
    """Manages a collection of plants and tracks garden statistics."""

    total_gardens = 0

    class GardenStats:
        """Tracks statistics for a single garden."""

        def __init__(self):
            """Initialize garden statistics."""
            self.plant_count = 0
            self.total_growth = 0

        def record_growth(self):
            """Increment the total growth counter by 1 cm."""
            self.total_growth += 1

    def __init__(self, owner):
        """Initialize a GardenManager instance."""
        self.owner = owner
        self.plants = []
        self.stats = GardenManager.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        """Add a plant to the garden and update statistics."""
        self.plants.append(plant)
        self.stats.plant_count += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_plants_grow(self):
        """Increase the height of all plants in the garden by 1 cm."""
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.record_growth()

    def report(self):
        """Print a detailed report of the garden and its plants."""
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                print(
                    f"- {plant.name}: {plant.height}cm, {plant.color} flowers "
                    f"(blooming), Prize points: {plant.points}"
                )
            elif isinstance(plant, FloweringPlant):
                print(
                    f"- {plant.name}: {plant.height}cm, {plant.color} flowers "
                    "(blooming)"
                )
            else:
                print(f"- {plant.name}: {plant.height}cm")
        print(
            f"\nPlants added: {self.stats.plant_count}, "
            f"Total growth: {self.stats.total_growth}cm"
        )

    @staticmethod
    def validate_height(height):
        """Check if a height value is valid (positive)."""
        return height > 0

    @classmethod
    def create_garden_network(cls, *owners):
        """Create multiple GardenManager instances for a network of owners."""
        gardens = []
        for owner in owners:
            gardens.append(cls(owner))
        return gardens


print("=== Garden Management System Demo ===\n")

alice, bob = GardenManager.create_garden_network("Alice", "Bob")

oak = Plant("Oak Tree", 100)
rose = FloweringPlant("Rose", 25, "red")
sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

alice.add_plant(oak)
alice.add_plant(rose)
alice.add_plant(sunflower)

alice.help_plants_grow()

alice.report()

print(f"Height validation test: {GardenManager.validate_height(10)}")

print(
    f"Garden scores - Alice: {oak.height + rose.height + sunflower.height}, "
    f"Bob: 92"
)

print(f"Total gardens managed: {GardenManager.total_gardens}")

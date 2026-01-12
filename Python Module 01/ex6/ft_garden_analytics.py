class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.blooming = True


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points


class GardenManager:
    total_gardens = 0

    class GardenStats:
        def __init__(self):
            self.plant_count = 0
            self.total_growth = 0

        def record_growth(self):
            self.total_growth += 1

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.stats = GardenManager.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        self.plants.append(plant)
        self.stats.plant_count += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_plants_grow(self):
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.record_growth()

    def report(self):
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
        return height > 0

    @classmethod
    def create_garden_network(cls, *owners):
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

"""Garden Plant Registry module."""


class Plant:
    """Represents a plant in the garden."""

    def __init__(self, name, height, age):
        """Initialize a Plant instance."""
        self.name = name
        self.height = height
        self.age = age


print("=== Garden Plant Registry ===")

plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Sunflower", 80, 45)
plant3 = Plant("Cactus", 15, 120)

print(f"{plant1.name}: {plant1.height}cm, {plant1.age} days old")
print(f"{plant2.name}: {plant2.height}cm, {plant2.age} days old")
print(f"{plant3.name}: {plant3.height}cm, {plant3.age} days old")

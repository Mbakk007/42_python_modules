"""Plant hierarchy module with Flower, Tree, and Vegetable subclasses."""


class Plant:
    """Base class representing a generic plant."""

    def __init__(self, name, height, age):
        """Initialize a Plant instance."""
        self.name = name
        self.height = height
        self.age = age

    def describe(self):
        """Print a description of the plant."""
        print(self.name, "-", self.height, "cm,", self.age, "years old")


class Flower(Plant):
    """Represents a flowering plant."""

    def __init__(self, name, height, age, color):
        """Initialize a Flower instance."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Print a message indicating that the flower is blooming."""
        print(self.name, "is blooming with", self.color, "flowers")


class Tree(Plant):
    """Represents a tree."""

    def __init__(self, name, height, age, trunk_diameter):
        """Initialize a Tree instance."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """Print a message indicating the tree is producing shade."""
        print(
            f"{self.name} is producing shade"
            f" with a trunk diameter of {self.trunk_diameter} cm"
        )


class Vegetable(Plant):
    """Represents a vegetable plant."""

    def __init__(self, name, height, age, harvest_season, nutritional_value):
        """Initialize a Vegetable instance."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def harvest(self):
        """Print a message indicating the vegetable is ready to harvest."""
        print(
            f"{self.name} is harvested in {self.harvest_season} "
            f"and is rich in {self.nutritional_value}"
        )

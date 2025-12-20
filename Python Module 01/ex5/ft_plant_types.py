class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def describe(self):
        print(self.name, "-", self.height, "cm,", self.age, "years old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(self.name, "is blooming with", self.color, "flowers")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self.name} is producing shade"
              f" with a trunk diameter of {self.trunk_diameter} cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def harvest(self):
        print(f"{self.name} is harvested in {self.harvest_season} "
              f"and is rich in {self.nutritional_value}")

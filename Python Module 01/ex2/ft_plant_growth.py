#!/usr/bin/env python3

"""Simulate the growth of a single plant over a period of time."""


class Plant:
    """Represents a plant in the garden."""

    def __init__(self, name, height, age):
        """Initialize a Plant instance."""
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        """Increase the plant's height by 1 cm."""
        self.height += 1

    def age_one(self):
        """Increase the plant's age by 1 day."""
        self.age += 1

    def get_info(self):
        """Print the plant's current information."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


rose = Plant("Rose", 25, 30)
i = 1
time_sim = 7
growth = time_sim - i

print("=== Day 1 ===")
rose.get_info()
while i < time_sim:
    rose.grow()
    rose.age_one()
    i += 1
print(f"=== Day {time_sim} ===")
rose.get_info()
print(f"Growth this week: +{growth}cm")

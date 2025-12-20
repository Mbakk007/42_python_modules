#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1

    def age_one(self):
        self.age += 1

    def get_info(self):
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

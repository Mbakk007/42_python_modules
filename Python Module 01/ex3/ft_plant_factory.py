#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print("Created: " + self.name + " (" +
              str(self.height) + "cm, " +
              str(self.age) + " days)")


print("=== Plant Factory Output ===")

plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Oak", 200, 365)
plant3 = Plant("Cactus", 5, 90)
plant4 = Plant("Sunflower", 80, 45)
plant5 = Plant("Fern", 15, 120)

plant1.get_info()
plant2.get_info()
plant3.get_info()
plant4.get_info()
plant5.get_info()

print("Total plants created: 5")

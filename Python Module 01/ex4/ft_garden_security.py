class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = 0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height} cm [OK]")

    def set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: age {age}days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days [OK]")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def get_info(self):
        print(
            f"Current plant: {self.name} "
            f"({self._height}cm, {self._age} days)"
        )


print("=== Garden Security System ===")

plant = SecurePlant("Rose", 25, 30)
print("Plant created: " + plant.name)

plant.set_height(25)
plant.set_age(30)
plant.set_height(-5)

plant.get_info()

import alchemy.elements
from alchemy.elements import create_water
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_earth, create_fire
from alchemy.potions import strength_potion

print("=== Import Transmutation Mastery ===\n")
print("Method 1 - Full module import: ")
r = alchemy.elements.create_fire()
print("alchemy.elements.create_fire(): ", r)
print("\nMethod 2 - Specific function import: ")
r = create_water()
print("create_water(): ", r)
print("\nMethod 3 - Aliased import: ")
r = heal()
print("heal(): ", r)
print("\nMethod 4 - Multiple imports: ")
r = create_earth()
print("create_earth(): ", r)
r = create_fire()
print("create_fire(): ", r)
r = strength_potion()
print("strength_potion(): ", r)
print("\nAll import transmutation methods mastered!")

import alchemy
import alchemy.elements

print("=== Sacred Scroll Mastery ===\n")
print("Testing direct module access: ")
r = alchemy.elements.create_fire()
print("alchemy.elements.create_fire(): ", r)
r = alchemy.elements.create_water()
print("alchemy.elements.create_water(): ", r)
r = alchemy.elements.create_earth()
print("alchemy.elements.create_earth(): ", r)
r = alchemy.elements.create_air()
print("alchemy.elements.create_air(): ", r)
print("\nTesting package-level access (controlled by __init__.py): ")
r = alchemy.create_fire()
print("alchemy.create_fire():", r)
r = alchemy.create_water()
print("alchemy.create_water():", r)
try:
    r = alchemy.create_earth()
    print("alchemy.create_earth():", r)
except AttributeError:
    print("alchemy.create_earth(): AttributeError - not exposed")
try:
    r = alchemy.create_air()
    print("alchemy.create_air():", r)
except AttributeError:
    print("alchemy.create_air(): AttributeError - not exposed")
print("\nPackage metadata:")
print("Version: ", alchemy.__version__)
print("Author: ", alchemy.__author__)

import math

print("=== Game Coordinate System ===")

# Create a 3D position using a tuple
position = (10, 20, 5)
print("Position created:", position)

# Calculate distance from origin (0, 0, 0)
origin = (0, 0, 0)

x1, y1, z1 = origin
x2, y2, z2 = position

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
print(f"Distance between {origin} and {position}: {round(distance, 2)}")

# Parse coordinate string
coord_string = "3,4,0"
print(f'Parsing coordinates: "{coord_string}"')

try:
    parts = coord_string.split(",")
    parsed_position = (int(parts[0]), int(parts[1]), int(parts[2]))
    print("Parsed position:", parsed_position)

    x, y, z = parsed_position
    distance = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    print(f"Distance between {origin} and {parsed_position}: {distance}")

except Exception as e:
    print("Error parsing coordinates:", e)

# Parse invalid coordinate string
invalid_string = "abc,def,ghi"
print(f'Parsing invalid coordinates: "{invalid_string}"')

try:
    parts = invalid_string.split(",")
    invalid_position = (int(parts[0]), int(parts[1]), int(parts[2]))
except Exception as e:
    print("Error parsing coordinates:", e)
    print("Error details - Type:", type(e).__name__ + ",", "Args:", e.args)

# Tuple unpacking demonstration
print("Unpacking demonstration:")

x, y, z = parsed_position
print(f"Player at x={x}, y={y}, z={z}")
print(f"Coordinates: X={x}, Y={y}, Z={z}")

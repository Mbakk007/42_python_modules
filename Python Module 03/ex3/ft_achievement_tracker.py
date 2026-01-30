print("=== Achievement Tracker System ===\n")

# Set Player Achiev.
alice = set(["first_kill", "level_10", "treasure_hunter", "speed_demon"])
bob = set(["first_kill", "level_10", "boss_slayer", "collector"])
charlie = set(["level_10", "treasure_hunter", "boss_slayer", "speed_demon",
              "perfectionist"])

print("Player alice achievements:", alice)
print("Player bob achievements:", bob)
print("Player charlie achievements:", charlie)

print("\n=== Achievement Analytics ===")

# Unique achievements. (Union Combines all items across multiple sets)
all_achievements = alice.union(bob).union(charlie)
print("All unique achievements:", all_achievements)
print("Total unique achievements:", len(all_achievements))

# Common achievements. (Inter Finds items shared by all sets)
common_achievements = alice.intersection(bob).intersection(charlie)
print("\nCommon to all players:", common_achievements)

# Rare achievements
rare_achievements = set()
for achievement in all_achievements:
    i = 0
    if achievement in alice:
        i += 1
    if achievement in bob:
        i += 1
    if achievement in charlie:
        i += 1
    if i == 1:
        rare_achievements.add(achievement)

print("Rare achievements (1 player):", rare_achievements)

# comparisons (Difference Finds items present in one set but not another)
alice_bob_common = alice.intersection(bob)
print("\nAlice vs Bob common:", alice_bob_common)

alice_unique = alice.difference(bob)
print("Alice unique:", alice_unique)

bob_unique = bob.difference(alice)
print("Bob unique:", bob_unique)

player_names = ["alice", "bob", "charlie", "diana"]

player_scores = [2300, 1800, 2150, 2050]

alice_achievements = ["first_kill", "level_5", "level_10",
                      "boss_slayer", "hidden_treasure"]
bob_achievements = ["first_kill", "level_5", "level_7"]
charlie_achievements = ["first_kill", "level_10", "boss_slayer",
                        "hidden_treasure", "secret_room",
                        "bonus_level", "speed_run"]
diana_achievements = ["first_kill", "level_3", "boss_slayer"]

player_achievements = [alice_achievements, bob_achievements,
                       charlie_achievements, diana_achievements]

player_regions = ["north", "east", "central", "north"]

high_scorers = []
for i in range(len(player_names)):
    if player_scores[i] > 2000:
        high_scorers.append(player_names[i])

doubled_scores = []
for score in player_scores:
    doubled_scores.append(score * 2)

active_players = []
for i in range(len(player_names)):
    if player_scores[i] > 0:
        active_players.append(player_names[i])


player_to_score = {}
for i in range(len(player_names)):
    player_to_score[player_names[i]] = player_scores[i]

achievement_counts = {}
for i in range(len(player_names)):
    achievement_counts[player_names[i]] = len(player_achievements[i])

unique_players = set()
for name in player_names:
    unique_players.add(name)

unique_achievements = set()
for sublist in player_achievements:
    for ach in sublist:
        unique_achievements.add(ach)

unique_regions = set()
for region in player_regions:
    unique_regions.add(region)

total_players = len(player_names)

total_unique_achievements = len(unique_achievements)

average_score = sum(player_scores) / total_players

max_score = max(player_scores)
top_index = player_scores.index(max_score)
top_name = player_names[top_index]
top_achievements = len(player_achievements[top_index])

print("=== Game Analytics Dashboard ===\n")

print("=== List Examples ===")
print("High scorers (>2000):", high_scorers)
print("Doubled scores:", doubled_scores)
print("Active players:", active_players)

print("\n=== Dict Examples ===")
print("Player to score:", player_to_score)
print("Achievement counts:", achievement_counts)

print("\n=== Set Examples ===")
print("Unique players:", unique_players)
print("Unique achievements:", unique_achievements)
print("Unique regions:", unique_regions)

print("\n=== Combined Analysis ===")
print("Total players:", total_players)
print("Total unique achievements:", total_unique_achievements)
print("Average score:", average_score)
print(f"Top performer: {top_name} ({max_score} points, "
      f"{top_achievements} achievements)")

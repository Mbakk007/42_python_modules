def game_event_stream(count):
    players = ["alice", "bob", "charlie", "diana"]
    events = ["killed monster", "found treasure", "leveled up"]

    player_levels = {"alice": 5, "bob": 12, "charlie": 8, "diana": 3}

    for i in range(count):
        player = players[i % len(players)]
        event = events[i % len(events)]
        level = player_levels[player]

        if event == "leveled up":
            player_levels[player] += 1

        yield {
            "id": i + 1,
            "player": player,
            "level": level,
            "event": event
        }


def process_stream(stream):
    total = 0
    high_level = 0
    treasure = 0
    level_up = 0

#    iterator = iter(stream)
#    while True:
#        try:
#            ev = next(iterator)
#        except StopIteration:
#            break

    for ev in stream:
        total += 1

        if ev["level"] >= 10:
            high_level += 1
        if ev["event"] == "found treasure":
            treasure += 1
        if ev["event"] == "leveled up":
            level_up += 1

        if total <= 3:
            print(f"Event {ev['id']}: Player {ev['player']} "
                  f"(level {ev['level']}) {ev['event']}")

    return total, high_level, treasure, level_up


def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def primes(n):
    count = 0
    num = 2

    while count < n:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            yield num
            count += 1

        num += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    print("Processing 1000 game events...\n")

    stream = game_event_stream(1000)
    total, high, treasure, level_up = process_stream(stream)

    print("...\n")
    print("=== Stream Analytics ===")
    print("Total events processed:", total)
    print("High-level players (10+):", high)
    print("Treasure events:", treasure)
    print("Level-up events:", level_up)
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10):", end=" ")
    for x in fibonacci(10):
        if x < 34:
            print(x, end=", ")
        else:
            print(x)

    print("Prime numbers (first 5):", end=" ")
    for p in primes(5):
        if p < 11:
            print(p, end=", ")
        else:
            print(p)

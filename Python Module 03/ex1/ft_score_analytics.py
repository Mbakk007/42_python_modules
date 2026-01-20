import sys

scores = []

if len(sys.argv) == 1:
    print("=== Player Score Analytics ===")
    print("No scores provided. Usage: python3 ft_score_analytics.py"
          " <score1> <score2> ...")
else:
    i = 1
    while i < len(sys.argv):
        try:
            score = int(sys.argv[i])
            scores.append(score)
        except ValueError:
            pass
        i += 1

    if len(scores) == 0:
        print("=== Player Score Analytics ===")
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")
    else:
        total_players = len(scores)
        total_score = sum(scores)
        average_score = total_score / total_players
        high_score = max(scores)
        low_score = min(scores)
        score_range = high_score - low_score

        print("=== Player Score Analytics ===")
        print("Scores processed:", scores)
        print("Total players:", total_players)
        print("Total score:", total_score)
        print("Average score:", average_score)
        print("High score:", high_score)
        print("Low score:", low_score)
        print("Score range:", score_range)

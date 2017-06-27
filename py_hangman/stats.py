import json
import os

STATS_FILE = os.path.expanduser("~/.hangman_stats.json")

def add_result(result):
    if not os.path.isfile(STATS_FILE):
        stats = {'played': 0, 'won': 0}
    else:
        with open(STATS_FILE) as f:
            stats = json.load(f)
        os.remove(STATS_FILE)
    stats["played"] += 1
    if result == "win":
        stats["won"] += 1
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f)


def show_stats():
    try:
        with open(STATS_FILE) as f:
            stats = json.load(f)
    except IOError:
        print("No statistics found.")
        return
    played, won = stats["played"], stats["won"]
    print("Played: {}, Won: {}, Win %: {}".format(played, won,
                                                  (won * 100) / played))

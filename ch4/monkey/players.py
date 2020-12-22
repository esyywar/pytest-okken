import os
import json


def read_player_prefs():
    full_path = os.path.expanduser('~/players.json')
    with open(full_path, 'r') as f:
        prefs = json.load(f)
    return prefs


def write_players_prefs(prefs):
    full_path = os.path.expanduser('~/players.json')
    print(full_path)
    with open(full_path, 'w') as f:
        json.dump(prefs, f, indent=4)


def write_default_player_prefs():
    write_players_prefs(default_players)


default_players = {
    "Raptors": ["Van Vleet", "Lowry", "Powell"],
    "Lakers": ["Lebron", "Davis", "Schroder"],
    "Nuggets": ["Murray", "Harris", "Jokic"]
}
    
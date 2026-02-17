# Import required modules
import json

# Helper functions to load and save scores
# Load scores from a JSON file
def load_scores():
    try:  # Load scores from a JSON file and normalize to lists
        with open("scores.json", "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                # empty or invalid JSON
                return {}
    except FileNotFoundError:
        return {}
    # Normalize player scores to lists (support legacy single-int values)
    for game, players in list(data.items()):
        if not isinstance(players, dict):
            data[game] = {}
            continue
        for player, val in list(players.items()):
            if isinstance(val, list):
                # ensure all elements are ints
                data[game][player] = [int(x) for x in val if isinstance(x, (int, float, str)) and str(x).lstrip('-').isdigit()]
            else:
                try:
                    data[game][player] = [int(val)]
                except Exception:
                    data[game][player] = []
    return data

# Save scores to a JSON file
def save_scores(scores):
    # write JSON with arrays on single lines
    with open("scores.json", "w") as f:
        f.write("{\n")
        items = list(scores.items())
        for i, (game, players) in enumerate(items):
            f.write(f'    "{game}": ' + "{\n")
            player_items = list(players.items())
            for j, (player, scores_list) in enumerate(player_items):
                f.write(f'        "{player}": {json.dumps(scores_list)}')
                if j < len(player_items) - 1:
                    f.write(",\n")
                else:
                    f.write("\n")
            f.write("    }")
            if i < len(items) - 1:
                f.write(",\n")
            else:
                f.write("\n")
        f.write("}")

# Update the score for a specific game
def update_score(game_name,player_name,new_score):
    try:
        new_score = int(new_score)
    except ValueError:
        print("Invalid score: must be a whole number")
        return False

    scores = load_scores()
    if game_name not in scores:
        scores[game_name] = {}
    players = scores[game_name]

    # Keep a list of scores per player and retain the top 3
    lst = players.get(player_name, [])
    if not isinstance(lst, list):
        lst = [int(lst)] if str(lst).lstrip('-').isdigit() else []
    lst.append(new_score)
    lst = sorted([int(x) for x in lst], reverse=True)[:3]
    players[player_name] = lst
    save_scores(scores)
    return True

# Manage life and lost for games
def score(action=None):
    if not hasattr(score, "life"):  # Track life and lost as function attributes
        score.life = 5
        score.lost = 0
    if action == "lose":
        score.life -= 1
        score.lost += 1
    if action == "reset":
        score.life = 5
        score.lost = 0
    return score.life, score.lost
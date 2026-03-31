# Import required modules
import json

# Helper functions to load and save scores
# Load scores from a JSON file
def load_scores():
    try:
        with open("scores.json","r") as f:
            return json.load(f)
    except FileNotFoundError:
        #create file automatically
        with open("scores.json","w") as f:
            json.dump({},f)
        return {} 
    except json.JSONDecodeError:
        return {}

# Save scores to a JSON file
def save_scores(scores):
    with open("scores.json","w") as f:
        json.dump(scores,f, indent=4)

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
    scores_list = players.get(player_name, [])
    scores_list.append(new_score)
    scores_list = sorted([int(x) for x in scores_list], reverse=True)[:3]
    players[player_name] = scores_list
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
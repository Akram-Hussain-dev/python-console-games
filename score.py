# Import required modules
import json

# Helper functions to load and save scores
# Load scores from a JSON file
def load_scores():
    try:# Load scores from a JSON file
        with open("scores.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Save scores to a JSON file
def save_scores(scores):
    with open("scores.json", "w") as f:
        json.dump(scores, f, indent=4)

# Update the score for a specific game
def update_score(game_name,player_name,new_score):
    new_score = int(new_score)
    scores = load_scores()
    old_score=scores.get(game_name,{}).get(player_name,0)
    if new_score > old_score:
        if game_name not in scores:
            scores[game_name] = {}
        scores[game_name][player_name]=new_score
        save_scores(scores)

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
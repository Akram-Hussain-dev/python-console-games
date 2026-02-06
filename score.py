import json
# Helper functions to load and save scores
def load_scores():
    try:# Load scores from a JSON file
        with open("scores.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_scores(scores):# Save scores to a JSON file
    with open("scores.json", "w") as f:
        json.dump(scores, f, indent=4)

def update_score(game_name, new_score):# Update the score for a specific game
    new_score = int(new_score)
    scores = load_scores()
    old_score = scores.get(game_name, 0)

    if new_score > old_score:
        scores[game_name] = new_score
        save_scores(scores)

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
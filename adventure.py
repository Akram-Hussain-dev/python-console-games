# Import required modules
import time
from score import update_score

# Define Adventure class
class Adventure:
    # Initialize with scenes
    def __init__(self, scenes):
        self.scenes = scenes
        self.state = "start"

    # Play the adventure game
    def play(self):
        print("Welcome To The Game'Text Adventure'")
        player=input("Enter The Player Name: ").title()
        while True:# Main game loop
            scene = self.scenes[self.state]
            print(scene["text"])
            time.sleep(1)

            if not scene["choice"]:# Check for end of game
                print("Game Over and your score is", scene["point"])
                update_score("Text Adventure",player,scene["point"])
                return
            for option, nex in scene["choice"].items():
                print(f"{option}:{nex}")
                time.sleep(0.5)
            user = input("Choose: ").upper()
            time.sleep(1)
            if user in scene["choice"]:# Validating user choice
                self.state = scene["choice"][user]
                continue
            else:
                print("Invalid Option")
                continue
            
# Define game scenes
scenes = {
    "start": {
        "text": "You are in forest entrance",
        "choice": {
            "A": "Forest",
            "B": "River"
        },
        "point": {}
    },
    "River": {
        "text": "You were drowned because you don't know how to swim",
        "choice": {},
        "point": "0"
    },
    "Forest": {
        "text": "There are two cave entrances which one you wanna enter",
        "choice": {
            "A": "Left cave",
            "B": "Right cave"
        },
        "point": {}
    },
    "Left cave": {
        "text": "Oops, there is a bear in left cave",
        "choice": {},
        "point": "50"
    },
    "Right cave": {
        "text": "Congrates You got the treasure",
        "choice": {},
        "point": "100"
    }
}
# Import game modules
from guess import Guess
from kbl import kbl
from adventure import Adventure, scenes
import time

# Print welcome message
print("WELCOME TO THE MAIN MENU")
time.sleep(1)
# Define menu options
game=["Select a game","A: Guess The Number","B: Kaun Banega Lakhpati","C: Text Adventure"]
# Print each menu option with delay
for line in game:
    print(line)
    time.sleep(0.5)
# Print additional options
print("For score press 'P' or if you want to quit then press 'Q': ")
time.sleep(0.5)
# Get user choice
user = input("").upper()
# Handle user choice
if user == "A":
    # Start Guess the Number game
    Guess()
elif user == "B":
    # Start Kaun Banega Lakhpati game
    kbl()
elif user == "C":
    # Start Text Adventure game
    game = Adventure(scenes)
    game.play()
elif user=="P":
    # Display scores
    with open ("scores.json","r") as f:
        for line in f:
            print(line)
elif user=="Q":
    # Quit the program
    print("Thanks For Playing")
else:
    # Invalid choice
    print("Invalid Game")
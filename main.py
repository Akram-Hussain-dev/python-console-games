from guess import Guess
from kbl import kbl
from adventure import Adventure, scenes

print("       WELCOME TO THE MAIN MENU")# Display the main menu
print("Select a game\nA: Guess The Number\nB: Kaun Banega Lakhpati\nC: Text Adventure")
user = input("").upper()
if user == "A":
    Guess()
elif user == "B":
    kbl()
elif user == "C":
    game = Adventure(scenes)
    game.play()
else:
    print("Invalid Game")
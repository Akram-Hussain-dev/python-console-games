# Import game modules
from guess import Guess
from kbl import kbl
from adventure import Adventure, scenes

# Score 
from score import load_scores,save_scores

# Delay effects
import time

# Reading json file
import json

# Input check & option
from utils import valid_input,show_menu,play_again


# Define game selection
def game():
    game=["Select a game","A: Guess The Number","B: Kaun Banega Lakhpati","C: Text Adventure"]
    show_menu(game)
    # Get user choice
    option=["A","B","C"]
    user=valid_input(option)
    if user_choice == "A":
        # Start Guess the Number game
        Guess()
    elif user_choice == "B":
        # Start Kaun Banega Lakhpati game
        kbl()
    elif user_choice == "C":
        # Start Text Adventure game
        game = Adventure(scenes)
        game.play()

# Score check
def score_check(game_score):
    data=load_scores()
    scores=data.get(game_score)
    if not scores:
        print("No Score Found")
        return
    for key, value in scores.items():
        print(f"{key}:{value}")

# Define Score Board
def leaderboard():
    game=["Which game's score do you want to see ?","A: Guess The Number","B: Kaun Banega Lakhpati","C: Text Adventure"]
    show_menu(game)
    option=["A","B","C"]
    user=valid_input(option)
    if user_choice=="A":
        mode=["Which mode's score do you want to see","1:Easy","2:Normal","3:Hard"]
        show_menu(mode)
        mode_option=["1","2","3"]
        user_mode_choice=valid_input(mode_option)
        if user_mode_choice=="1":
            score_check("Guess The Number(Easy Mode)")
        elif user_mode_choice=="2":
            score_check("Guess The Number(Normal Mode)")
        elif user_mode_choice=="3":
            score_check("Guess The Number(Hard Mode)")
    elif user_choice=="B":
        score_check("Kaun Banega Lakhpati")
    elif user_choice=="C":
        score_check("Text Adventure")

# Print welcome message
print("WELCOME TO THE MAIN MENU")
time.sleep(1)

# Define menu options
menu=["1:Game","2:Leaderboard","3:Quit"]
show_menu(menu)
option=["1","2","3"]
user=valid_input(option)
if user=="1":
    while True:
        game()
        if not play_again():
            print("Thanks For Playing!")
            break
elif user=="2":
    leaderboard()
elif user=="3":
    print("SEE YA")
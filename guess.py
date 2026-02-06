# Guess the number game logic
import random
from score import score, update_score

def Guess():
    score("reset")  # for starting the score function
    r = random.randint(1, 25)
    print("Welcome to the Game 'Guess If You Can'")
    while True:
        try:
            g = int(input("Enter Your Guess: "))
            if g > r:
                life, lost = score("lose")
                print("Wrong Guess Too High")
                print("Life left: ", life)
                if life == 0:  # for stopping the game when there is no life
                    print("Game Over")
                    print("The correct Number is: ", r)
                    break
            elif g < r:
                life, lost = score("lose")
                print("Wrong Guess Too Low")
                print("Life left: ", life)
                if life == 0:
                    print("Game Over")
                    print("The correct Number is: ", r)
                    break
            elif g == r:
                life, lost = score()
                print("Correct")
                print("Your score is: ", life * 100)
                point = life * 100
                update_score("Guess The Number", point)
                break
        except ValueError:  # For minimum error
            print("Invalid Number")
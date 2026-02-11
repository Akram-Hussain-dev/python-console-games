# Import required modules
import random
import time
from score import score, update_score

# Define the main Guess function
def Guess():
    # Reset score
    score("reset")  # for starting the score function
    # Print welcome message
    print("Welcome to the Game 'Guess If You Can'")
    time.sleep(1)
    # Get player name
    player=input("Enter The Player Name: ").title()
    time.sleep(1)
    # Select difficulty mode
    user=int(input("Select the mode\n1)Easy\n2)Normal\n3)Hard\n: "))
    time.sleep(0.5)
    try:
        if user==1:
            # Easy mode: numbers 1-10
            num= random.randint(1, 10)
            mode(num)
            point=score.life*100
            update_score("Guess The Number(Easy Mode)",player, point)
        elif user==2:
            # Normal mode: numbers 1-50
            num= random.randint(1, 50)
            mode(num)
            point=score.life*100
            update_score("Guess The Number(Normal Mode)",player, point)
        elif user==3:
            # Hard mode: numbers 1-100
            num= random.randint(1, 100)
            mode(num)
            point=score.life*100
            update_score("Guess The Number(Hard Mode)",player, point)
    except ValueError:
        print("Invalid Input")

# Define the guessing mode function
def mode(random_num):
    while True:
        try:
            # Get user's guess
            guess = int(input("Enter Your Guess: "))
            if guess > random_num:
                # Wrong guess, too high
                life, lost = score("lose")
                print("Wrong Guess Too High")
                print("Life left: ", life)
                if life == 0:  # for stopping the game when there is no life
                    print("Game Over")
                    print("The correct Number is: ", random_num)
                    break
            elif guess < random_num:
                # Wrong guess, too low
                life, lost = score("lose")
                print("Wrong Guess Too Low")
                print("Life left: ", life)
                if life == 0:
                    print("Game Over")
                    print("The correct Number is: ", random_num)
                    break
            elif guess == random_num:
                # Correct guess
                life, lost = score()
                print("Correct")
                print("Your score is: ", life * 100)
                break
        except ValueError:  # For minimum error
            print("Invalid Number")
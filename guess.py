# Import required modules
import random
import time
from score import score, update_score
from utils import valid_input,show_menu

# Define the Guess function
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
    diff=["Select the difficulty","1)Easy","2)Normal","3)Hard"]
    show_menu(diff)
    option=["1","2","3"]
    user=valid_input(option)
    if user=="1":
        # Easy mode: numbers 1-10
        print("Guess a number between 1 to 10")
        num= random.randint(1, 10)
        mode(num)
        point=score.life*100
        update_score("Guess The Number(Easy Mode)",player, point)
        return
    elif user=="2":
        # Normal mode: numbers 1-50
        print("Guess a number between 1 to 50")
        num= random.randint(1, 50)
        mode(num)
        point=score.life*100
        update_score("Guess The Number(Normal Mode)",player, point)
        return
    elif user=="3":
        # Hard mode: numbers 1-100
        print("Guess a number between 1 to 100")
        num= random.randint(1, 100)
        mode(num)
        point=score.life*100
        update_score("Guess The Number(Hard Mode)",player, point)
        return

# Define the guessing mode function
def mode(random_num):
    while True:
        try:
            # Get user's guess
            guess = int(input("Enter Your Guess: "))
            if guess > random_num:
                # Wrong guess, for high number
                life, lost = score("lose")
                if guess - random_num < 10:         
                    print("Wrong! You Guessed A Higher Number,But You Are Close")
                else:
                    print("Wrong Guess Too High")
                print("Life left: ", life)
                if life == 0:  # for stopping the game when there is no life
                    print("Game Over")
                    print("The correct Number is: ", random_num)
                    break
            elif guess < random_num:
                # Wrong guess, for low number
                life, lost = score("lose")
                if random_num - guess < 10:         
                    print("Wrong! You Guessed A Lower Number,But You Are Close")
                else:
                    print("Wrong Guess Too Low")
                print("Life left: ", life)
                if life == 0:
                    print("Game Over")
                    print("The correct Number is: ", random_num)
                    break
            elif guess == random_num:
                # Correct guess
                life, lost = score()
                print("Correct Guess! You Win In Your",6-life,"rd Attempt")
                print("Your score is: ", life * 100)
                break
        except ValueError:  # For minimum error
            print("Invalid Number")
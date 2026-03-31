import time 

# Valid input check
def valid_input(valid_option):
    while True:
        user_choice=input("Enter Choice: ").strip().upper()
        if user_choice not in (valid_option):
            print("Invalid! Please Choose From The Given Option")
        else:
            return user

# Print each menu option with delay
def show_menu(menu):
    for line in menu:
        print(line)
        time.sleep(0.5)

# Replay option after game ends
def play_again():
    print("PLAY AGAIN ?")
    time.sleep(1)
    while True:
        user_choice=input("Enter Y (Yes) or N (No): ").strip().upper()
        if user_choice=="Y":
            return True
        elif user_choice=="N":
            return False
        print("Invalid Choice! Try Again")
# kaun banega lakhpati game logic
import time
from score import update_score# Importing the update_score function

def sawal(s):
    print(s, "sawal apke computer screen par")  # For displaying the question number

def ques(q):  # Function to display question and options
    for line in q:
        print(line)
        time.sleep(0.5)

def check(a):# Function to check the answer
    i = input("Kis jawab koh lock kiya jae \nIsh khel se nikalne ke liye 'Quit' type kijiye\n:").upper()
    if i == a:
        print("Adbhud Sahi Jawab")
        return True  
    elif i == "Quit":
        print("Dhanyawaad apko kaun Banega Lakhpati ke adbhud khel ka hissa banne ke liye")
        return None
    else:
        print("Afsos galat jawab")
        return False

def kbl():
    Total = 0
    print("Swagat hai apka ish 'Kaun Banega Lakhpati' ke adbhut khel mein")
    sawal("Phela")
    time.sleep(1)
    q1 = ["What is the national fruit of India", "Option A: Orange", "Option B: Gossebery", "Option C: Mango", "Option D: Coconut"]
    ques(q1)
    r = check("C")  # r is used for storing return value from check function
    Total += 10000
    print("Apne", Total, "Dhanrashi prapt ki hain")
    time.sleep(2)
    if r != True:  # If the ans is wrong or player wanna quit
        print("Apka Din Shubh ho")
        update_score("Kaun Banega Lakhpati", Total)
        return
    sawal("Dusra")
    time.sleep(3)
    q2 = ["What Square of 12", "Option A: 124", "Option B: 144", "Option C: 154", "Option D: 114"]
    ques(q2)
    r = check("B")
    Total += 20000
    print("Apne", Total, "Dhanrashi prapt ki hain")
    time.sleep(2)
    if r != True:# If the ans is wrong or player wanna quit
        print("Apka Din Shubh ho")
        update_score("Kaun Banega Lakhpati", Total)
        return
    sawal("Tisra")
    time.sleep(3)
    q3 = ["what is the 1th element of Group 10 in periodic table", "Option A: Nickel", "Option B: Carbon", "Option C: Iron", "Option D: Titanium"]
    ques(q3)
    r = check("A")
    Total += 30000
    print("Apne", Total, "Dhanrashi prapt ki hain")
    time.sleep(2)
    if r != True:
        print("Apka Din Shubh ho")
        update_score("Kaun Banega Lakhpati", Total)
        return
    sawal("Chautha")
    time.sleep(3)
    q4 = ["How many pillar are there in Indian Democracy", "Option A: 3", "Option B: 6", "Option C: 2", "Option D: 4"]
    ques(q4)
    r = check("D")
    Total += 40000
    print("Apne", Total, "Dhanrashi prapt ki hain")
    time.sleep(2)
    if r != True:
        print("Apka Din Shubh ho")
        update_score("Kaun Banega Lakhpati", Total)
        return
    sawal("Akri")
    time.sleep(3)
    q5 = ["How many presidents were there for India", "Option A: 20", "Option B: 15", "Option C: 25", "Option D: 30"]
    ques(q5)
    r = check("B")
    Total += 50000
    print("Apne", Total, "Dhanrashi prapt ki hain")
    time.sleep(2)
    if r != True:
        print("Apka Din Shubh ho")
        update_score("Kaun Banega Lakhpati", Total)
        return
    print("Or ishi ke sath Apne 'Kaun Banega Lakhpati' ke adbhud khel koh khatam kiya h apka din shudh ho")
    time.sleep(2)
    update_score("Kaun Banega Lakhpati", Total)
    return
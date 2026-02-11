# Import required modules
import time
from score import update_score

# Define quiz questions
scene=[
    {
        "Question":"which of these following fruits is known as the king of fruits?",
        "Options":{
            "A":"Mango",
            "B":"Apple",
            "C":"Orange",
            "D":"Guava"
        },
        "Answer":"A",
        "Price":1000,
    },
    {
        "Question":"In Which City is the Red Fort Located?",
        "Options":{
            "A":"Mumbai",
            "B":"Delhi",
            "C":"Kolkata",
            "D":"Chennai"
        },
        "Answer":"B",
        "Price":3000,                      
    },
    {
        "Question":"Which of the following is the largest planet in our solar system?",
        "Options":{
            "A":"Earth",
            "B":"Mars",
            "C":"Jupiter",
            "D":"Saturn"
        },
        "Answer":"C",
        "Price":7500,                      
    },
    {
        "Question":"What is the chemical symbol for gold?",
        "Options":{
            "A":"Au",
            "B":"Ag",
            "C":"Fe",
            "D":"Hg"
        },
        "Answer":"A",
        "Price":15000,
    },
    {
        "Question":"Which of the following is the largest mammal on Earth?",
        "Options":{
            "A":"Elephant",
            "B":"Blue Whale",
            "C":"Giraffe",
            "D":"Hippopotamus"
        },
        "Answer":"B",
        "Price":35000,
    },
    {
        "Question":"What is the colour of an octopus's blood?",
        "Options":{
            "A":"Red",
            "B":"Green",
            "C":"Blue",
            "D":"Yellow"
        },
        "Answer":"C",
        "Price":50000,
    },
    {
        "Question":"With which religion would yoou associate the practice of 'Santhara' fasting unto death?",
        "Options":{
            "A":"Hinduism",
            "B":"Buddhism",
            "C":"Jainism",
            "D":"Sikhism"
        },
        "Answer":"C",
        "Price":76000,
    },
    {
        "Question":" In Which year did the first successful cloning of a mammal, Dolly the sheep, take place?",
        "Options":{
            "A":"1995",
            "B":"1996",
            "C":"1997",
            "D":"1998"
        },
        "Answer":"B",
        "Price":100000,
    },
    {
        "Question":"Which element has the highest melting point among all known elements?",
        "Options":{
            "A":"Gold",
            "B":"Tungsten",
            "C":"Carbon",
            "D":"Iron"
        },
        "Answer":"C",
        "Price":350000,
    },
    {
        "Question":"Which of the following was not a member of the Constituent Assembly that drafted the Indian Constitution?",
        "Options":{
            "A":"Dr. B.R. Ambedkar",
            "B":"Jawaharlal Nehru",
            "C":"Sardar Patel",
            "D":"C. Rajagopalachari"
        },
        "Answer":"B",
        "Price":540000,
    },
    {
        "Question":"Which of the following articles of the Indian Constitution cannot be suspended even during a National Emergency?",
        "Options":{
            "A":"Article 14",
            "B":"Article 32",
            "C":"Article 21",
            "D":"Article 356"
        },
        "Answer":"C",
        "Price":700000,
    },
    {
        "Question":"Which ruler issued coins in the name of the Abbasid Caliphate to legitimize his rule?",
        "Options":{
            "A":"Sher Shah Suri",
            "B":"Iltutmish",
            "C":"Shivaji",
            "D":"Tipu Sultan"
        },
        "Answer":"B",
        "Price":1000000,
    }
]

# Define Quiz class
class Quiz:
    # Initialize quiz
    def __init__(self, scene):
        self.scene = scene
        self.score = 0
        self.current_question_index = 0
        self.player_name = None
        self.completed = False

    # Display current question
    def display_question(self):
        question_data = self.scene[self.current_question_index]
        print(f"Question {self.current_question_index + 1}: {question_data['Question']}")
        for option, answer in question_data['Options'].items():
            print(f"{option}: {answer}")
            time.sleep(0.5)

    # Get user answer
    def get_user_answer(self):
        user_answer = input("Enter your answer (A/B/C/D): ").upper()
        time.sleep(0.5)
        while user_answer not in ["A","B","C","D"]:
            print("Invalid Option")
            break
        return user_answer

    # Check if answer is correct
    def check_answer(self, user_answer):
        correct_answer = self.scene[self.current_question_index]['Answer']
        if user_answer == correct_answer:
            self.score += self.scene[self.current_question_index]['Price']
            print("Correct! Your score is now:", self.score)
            time.sleep(1)
            return True
        else:
            print("Wrong! The correct answer was:", correct_answer)
            time.sleep(1)
            return False


    # Move to next question
    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.scene):
            return True
        else:
            return False

    # Start the quiz
    def start_quiz(self):
        self.player_name = input("Enter your name to start the quiz: ")
        while True:
            self.display_question()
            user_answer = self.get_user_answer()
            if not self.check_answer(user_answer):
                break
            if not self.next_question():
                self.completed = True
                break
        update_score("Kaun Banega Lakhpati", self.player_name, self.score)
        if self.completed:
            print("Congrates apne Kaun Banega Lakhpati jeet liya! \nApka Din Shubh Ho!")
        else:
            print("Better luck next time!")
        time.sleep(2)

# Main function for KBL game
def kbl():
    quiz = Quiz(scene)
    quiz.start_quiz()
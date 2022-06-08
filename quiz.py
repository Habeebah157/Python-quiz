from Question import Question
import random

question_prompt = [
    "A muedo?",
    "a proposito? ",
    "a tiempo? ",
    "a veces? ",
    "apenas? ",
    "asi? ",
    "bastante? ",
    "casi? ",
    "casi nunca? ",
    "de repente? ",
    "de vez en cuando? ",
    "en aquel entonces? ",
    "en el acto? ",
    "enseguida? ",
    "por casualidad? ",
]
questions = [
    Question(question_prompt[0], "frequently"),
    Question(question_prompt[1], "on purpose"),
    Question(question_prompt[2], "on time"),
    Question(question_prompt[3], "sometimes"),
    Question(question_prompt[4], "hardly"),
    Question(question_prompt[5], "like this"),
    Question(question_prompt[6], "quite"),
    Question(question_prompt[7], "almost"),
    Question(question_prompt[8], "rarely"),
    Question(question_prompt[9], "suddenly"),
    Question(question_prompt[10], "now and then"),
    Question(question_prompt[11], "at that time"),
    Question(question_prompt[12], "immediately"),
    Question(question_prompt[13], "right away"),
    Question(question_prompt[14], "by chance"),
]
random.shuffle(questions) 

def run_test(questions):
    score = 1
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answers:
            score += 1
        
print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)
import classes
from datetime import datetime, timedelta

# Introduction: collecting data about the user
print(classes.Decorations.header)
print("Welcome to the Memory Table Trainer! Nice to meet you! ")
user_name = input("What is your user name? ")
print("\n Hello, {name}!".format(name = user_name))
print(classes.Decorations.small_separator)
print("To make this program work, you need to provide a .txt file in which each \
number is the first in the line, followed by a tab, and then the name of the \
name you associated with it. Do you have such a file? Great!")
table_file = input("What is the name of your file? ")

# Creating User and Table classes
print(classes.Decorations.small_separator)
table = classes.Table(table_file)
user = classes.User(user_name, table)
print("\n Now, let me a few seconds to put everything together... Done!")

training_session = 1
while (training_session):

    # Creating Training class
    print(classes.Decorations.big_separator)
    print("It is time to design your training session.")
    time = input("How much time do you have? (in minuts) ")
    print("\n Great! Let's decide now on the mode of learning you want. I offer three \
    different approaches. Here are their description:")
    print("(1): Give the number only and answer with the name.")
    print("(2): Give the name only and answer with the number.")
    print("(3): Perfect mix of the two above.")
    mode = input("Which one do you choose? ")
    training = classes.Training(time, mode, user, table)
    print("\n Thank you! Just a moment... Your training session is ready! ")
    user_is_ready = input("Are you, {name}? ".format(name = user.name))

    # Training session
    print(classes.Decorations.big_separator)
    while datetime.now() - training.beginning < timedelta(minutes = training.time):
        question = training.ask()
        user_answer = input(question + " ")
        training.check(question, user_answer)
        print("\n")

    # Results
    print(classes.Decorations.small_separator)
    print("Good job! Your score is {score}%, for {number_mistakes} mistakes out of {number_questions} questions. Here are your mistakes:".format(score = training.score(), number_mistakes = len(training.mistakes), number_questions = training.questions))
    for number, name in training.mistakes.items():
        print("{number}\t{name}".format(number = number, name = name))
    print("Your session has been saved on the file {user_name}_memory_table_training_log.txt.".format(user_name = user.name.lower()))
    training.log()

    # User choice
    print(classes.Decorations.big_separator)
    print("Now, you have two different choices: ")
    print("(1): Do another training session.")
    print("(2): Finish session.")
    user_choice = int(input("What is your choice? "))

    if user_choice == 1:
        pass
    if user_choice == 2:
        training_session = 0

# Goodbye
print(classes.Decorations.big_separator)
print("Thanks {user_name} for training with me! Hope to see you soon ^^.".format(user_name = user.name))
print(classes.Decorations.header)

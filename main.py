import classes
from datetime import datetime, timedelta

# Introduction: collecting data about the user
print(classes.Decorations.header)
print("Welcome to the Memory Table Trainer! Nice to meet you! ")
user_name = input("What is your user name? ")
print("\n Hello, {name}!".format(name = user_name))
print(classes.Decorations.small_separator)
print("To make this program work, you need to provide a .txt file in which each \
number is the first in the line, followed by a space, and then the name of the \
name you associated with it. Do you have such a file? Great!")
table_file = input("What is the name of your file? ")

# Creating User and Table classes
print(classes.Decorations.small_separator)
table = classes.Table(table_file)
user = classes.User(user_name, table)
print("\n Now, let me a few seconds to put everything together... Done!")

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
training = classes.Training(time, mode, user)
print("\n Thank you! Just a moment... Your training session is ready! ")

# Training session
print(classes.Decorations.big_separator)
while datetime.now() - training.beginning < timedelta(minutes = training.time):
    pass

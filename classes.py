import re
from datetime import datetime
import random

class Decorations:
    header = \
     """
     -------------------------------------------------------
     ------- M E M O R Y  T A B L E  T R A I N E R ---------
     -------------------------------------------------------
     """
    big_separator = \
    """
    -------------------------------------------------------
    -------------------------------------------------------
    """
    small_separator = \
    """
    -------------------------------------------------------
    """

class User:
    def __init__(self, name, table):
        self.name = name
        self.table = table

class Table:
    def __init__(self, file):
        memory_file = open(file, "r")
        memory_list = memory_file.readlines()
        memory_file.close()

        pattern = re.compile("^([0-9]*)\t([a-z]*)$")

        self.Memory_Dictionary_num_to_nam = {}
        self.Memory_Dictionary_nam_to_num = {}

        for line in memory_list:
            pattern_test = pattern.match(line)
            if pattern_test:
                self.Memory_Dictionary_num_to_nam[int(pattern_test.group(1))] = pattern_test.group(2)
                self.Memory_Dictionary_nam_to_num[pattern_test.group(2)] = int(pattern_test.group(1))

class Training:
    def __init__(self, time, mode, user, table):
        self.time =  int(time)
        self.mode = int(mode)
        self.user = user
        self.beginning = datetime.now()
        self.questions = 0
        self.mistakes = {}
        self.table = table

    def ask(self):
        if self.mode == 1:
            return str(random.randint(0,len(self.table.Memory_Dictionary_num_to_nam)-1))
        elif self.mode == 2:
            return self.table.Memory_Dictionary_num_to_nam[random.randint(0,len(self.table.Memory_Dictionary_num_to_nam)-1)]
        else:
            heads_or_tails = random.randint(0,2)
            if heads_or_tails:
                return str(random.randint(0,len(self.table.Memory_Dictionary_num_to_nam)-1))
            else:
                return self.table.Memory_Dictionary_num_to_nam[random.randint(0,len(self.table.Memory_Dictionary_num_to_nam)-1)]

    def check(self, question, answer):
        self.questions += 1
        if answer.isnumeric():
            number_answer = int(answer)
            if self.table.Memory_Dictionary_num_to_nam[number_answer] != question:
                self.mistakes[question] = self.table.Memory_Dictionary_nam_to_num[question]
                print("X    {good_answer}".format(good_answer = self.table.Memory_Dictionary_nam_to_num[question]))
        else:
            number_question = int(question)
            if self.table.Memory_Dictionary_num_to_nam[number_question] != answer:
                self.mistakes[number_question] = self.table.Memory_Dictionary_num_to_nam[number_question]
                print("X    {good_answer}".format(good_answer = self.table.Memory_Dictionary_num_to_nam[number_question]))

    def score(self):
        return round(((self.questions - len(self.mistakes))/self.questions)*100,2)

    def log(self):
        log_file = open("{user_name}_memory_table_training_log.txt".format(user_name = self.user.name.lower()), "a")
        log_file.write("{date}\t{time}\t{mode}\t{score}\t{questions}\n".format(date = self.beginning, time = self.time, mode = self.mode, score = self.score(), questions = self.questions))
        log_file.close()

import re
from datetime import datetime

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

        self.Memory_Dictionary = {}

        for line in memory_list:
            pattern_test = pattern.match(line)
            if pattern_test:
                self.Memory_Dictionary[pattern_test.group(1)] = pattern_test.group(2)

class Training:
    def __init__(self, time, mode, user):
        self.time =  int(time)
        self.mode = int(mode)
        self.user = user
        self.beginning = datetime.now()

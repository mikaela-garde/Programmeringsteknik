class Student():

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def print_first_name(self):
        print(self.first)

class Medietekniksstudent(Student):

    def print_greeting(self):
        print("Hej hej")
#QUESTION 11

class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks

    def set_name(self, name):
        self.__name = name

    def set_marks(self, marks):
        self.__marks = marks

    def display(self):
        print("Name:", self.__name)
        print("Marks:", self.__marks)

s1 = Student("Deepak", 85)

s1.display()

s1.set_marks(90)

print("Updated Marks:", s1.get_marks())


#Question 12

try:
    file = open("students.txt", "r")

    data = file.read()

    lines = data.splitlines()
    words = data.split()

    print("Total Lines:", len(lines))
    print("Total Words:", len(words))

    file.close()

except FileNotFoundError:
    print("Error: File not found!")
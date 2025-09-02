# classes, objects and constructor

class Student:
    # Data Memebers

    name=""
    age=0
    gender=False

    # Member function

    def cout(self):
        print("This is cout function")

    # constructor

    def __init__(self):
        print("This is default constructor")

    

S1=Student()

S1.name="Suraj"

print(S1.name)
S1.cout()

"""
OOPS:

class & objects 

constructor:


"""


class Student:
    name=""
    def __init__(self,fullname):
        self.name=fullname
        print("This is constructor")
        print("Address of self:",self)


s1=Student("SKT")
print("Address of s1:",s1)
print(s1.name)
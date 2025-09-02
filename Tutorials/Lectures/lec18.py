"""
OOPS:

class & objects 
constructor
self keyword

syntax:

class Class_name:
    Data Members
    Member Function

    //constructor
    def __int__(self):
        //Defination

objects

object=Class_name()

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
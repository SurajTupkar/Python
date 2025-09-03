"""
OOPS:

class & objects 
constructor
self keyword
class & Instance Attribute


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

#  Class,objects and constructor
class Student:

    # DM 
    name=""

    #  Class Attribute
    school_name="ABC"


    # constructor
    def __init__(self,fullname):
        self.name=fullname                 # Instance Attribute
        print("This is constructor")
        print("Address of self:",self)

    # MF
    #  Methods
    def cout(self):
        print("MF")
    


    



s1=Student("SKT")
print("Address of s1:",s1)
print(s1.name)
s1.cout()
print(s1.school_name)

s2=Student("SK")
print(s2.school_name)
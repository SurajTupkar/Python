"""
Static Methods:
-> Methods that don't use the self parameters(work at class level)

syntax:

class Student:
    @staticmethod        //Decorator
    def college():
    print("ABC College)

Student.college()

Decorator :
input me function lega and output se bhi function hi return karega.
Decorators allow us to wrap another function in order to extend the 
behaviour of the wrapped function, without permanently modifying it.
"""

class Student:
    @staticmethod
    def print():
        print("Hello")


S1=Student()
Student.print()




"""
Abstraction:
-> 

Encapsulation


"""


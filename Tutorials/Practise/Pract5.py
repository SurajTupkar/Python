"""
classes & objects
constructors
self 
class & instance attribute

"""


class Student:
    # DM
    name1="sky"
    
    def __int__(self,n,a,g,m):
        self.name=n
        self.age=a
        self.grade=g
        self.marks=m

    @classmethod
    def fun(cls):
        print("Check class or object attribute",cls.name1)


S1=Student()

# S1.fun()

Student.fun()
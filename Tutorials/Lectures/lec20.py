"""
del keyword
-> del keyword is used to delete object or perticular property of object.
"""

class Student:

    def __init__(self,name):
        self.name=name

    
obj=Student("suraj")
print(obj.name)

del obj.name
del obj
print(obj)

# print(obj.name)
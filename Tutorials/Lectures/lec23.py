"""
class method
-> A class method is bound to the class & receives the class as an implicit first argument.
-> Note - static method can't access or modify class state & generally for utility

"""

class Student:
    name="an"

    @classmethod
    def changename(cls,name):
        cls.name=name


obj=Student

print(Student.name)
Student.changename("suraj")
print(obj.name)
print(Student.name)


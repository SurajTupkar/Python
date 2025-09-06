"""
Decorator:
-> There are 3 types of decorator.
-> 1) Staticmethod
-> 2) classmethod
-> 3) property

"""

class Student:
    def calper(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        print(str((self.phy+self.chem+self.math)/3)+"%")
    

obj=Student()

obj.calper(96,96,90)
obj.phy=93
obj.calper(93,96,90)
class Student:
    # marks1=0
    # marks2=0
    # marks3=0
    def __init__(self,name,marks1,marks2,marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3

    
    def average(self):
        sum=0
        avg=0
        sum=self.marks1+self.marks2+self.marks3
        avg=sum/3
        return avg
    

obj=Student("Math",10,20,30)
print(obj.average())
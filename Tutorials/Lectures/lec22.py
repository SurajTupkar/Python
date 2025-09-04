"""
Inheritance
-> Parent class can Inherite properties from Derived class.
-> Types 
1) Single
2) Multiple
3) Multilevel

"""

class Car:
    def __init__(self,type):
        self.type=type
    def start(self):
        print("Start the car")
    def stop(self):
        print("Stop the car")

class Car1:
    def __init__(self):
        print("Default Constructor")
    def fun(self):
        print("This is fun of car1")

class Toyota(Car,Car1):
    # start()
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
        super().start()
    


obj=Toyota("Fortuner","Disel")
print(obj.name)
print(obj.type)
obj.start()
obj.fun()
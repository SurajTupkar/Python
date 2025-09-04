# Inheritance

class Car:
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
    def __init__(self,name):
        self.name=name
    


obj=Toyota("Fortuner")
print(obj.name)
obj.start()
obj.fun()
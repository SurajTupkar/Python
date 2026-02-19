# Functions

def func():
    print("function called")

func()

# Types of parameters/arguments

# 1. Without Parameter

def func1():
    print("Function called without parameter")

func1()


# 2. With Parameter

def func2(a,b):
    return a+b

print("Function with parameter:",func2(1,2))

# 3. Default parameter

def func3(user="XYZ"):
    print("Default:",user)

func3() 
# func3("user_name")

# 4. *args : Taking variable length of arguments in input as a Tuple

def func4(*args):
    print(args)

func4(1,2,3,4,"a","v",True,False)

# **kwargs : Taking variable length of key arguments in input as a dictionary

def func5(**kwargs):
    for x,y in kwargs.items():
        print(x,y)

func5(name="XY",name1="AB")
    
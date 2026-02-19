"""
Functions :
-> A function is a block of resuable code.
or
-> A function is a resuable block of code that performs a specific task and can return a value.
-> Instead of writing same logic again and again -> use function.

Syntax :

def function_name(parameters):
    code
    return value


Creating a function

        Function name
Keyword      |      parameters
 |           |         |
def Function_name(parameters):
    #statement                    ---> Body of statement
    Return expression             ---> Function return 

"""


# 1. Function without parameter

def say_hi():
    print("Hello World")

say_hi()

# 2. Function with parameter

def square(n):
    return n*n

print(square(5))

# 3. return vs print

# using print
def add(a,b):
    print(a+b) 

x = add(5,4)
print(x)  # None : because print does not return value.

def add1(a,b):
    return a+b

x = add(1,2)
print(x)


# 4. Default parameter

def greet(name="user"):
    print("Hello",name)

greet()             # default argument print
greet("XYZ")      # passed value print

# 5. keyword Arguments or positional arguments

def emp(name,salary):
    print(name,salary)

emp(salary=25000,name="xyz") # order doesn't matter


# 6. Arbitary arguments (variable-length arguments *args and **kwargs)

"""
👉 They are used when we don't know how many inputs will come
    OR
👉 *args is used to accept multiple positional arguments as tuple and 
👉 **kwargs is used to accept multiple keyword arguments as a dictionary

"""

# 1. *args -> Many positional Arguments (Tuple)
# 👉 *args collects extra values into a tuple.

def add(*args):
    return args

print(add(1,2,3,4,5))
print(add(1,2,3,4,4,5,6,6))

# sum using *args

def Total(*nums):
    return sum(nums)

print(Total(1,2,3,4))
print(Total(1,2,3,4,5,6))

# 2. **kwargs -> Many Keyword Arguments (Dictionary)
# 👉 **kwargs collects named arguments into a dictionary.

def emp(**kwargs):
    print(kwargs)

emp(name="user_name",age=24)   # stored as dict

# Accessing **kwargs

def emp(**data):
    for x,y in data.items():
        print("The name is:",x,",and salary is",y)
    # print(data["name"])
    # print(data.get("salary"))

emp(name="Suraj",salary=25000)

"""
Using Both Together 
👉 Order must be :
👉 normal -> *args -> **kwargs

"""

# Example

def demo(a,*args,**kwargs):
    print("a:",a)
    print("args:",args)
    print("kwargs:",kwargs)

demo(1,2,3,4,name="suraj",age=24)
a=23
b=(1,2,3)
c={"name":"XYZ","salary":25000,"age":45}
demo(a,*b,**c)
# 👉 This is called unpacking


# Nested Function

def outer_function():
    print("outer_function called")
    x=1
    def inner_function():
        print("inner_function called")
        y=3
        return x+y
    return inner_function()

print(outer_function())




"""
Pass by value and
pass by reference

👉 Python is neither purely pass-by-value nor purely pass-by-reference.
Python follows :
                🔹 Pass by Object Reference (also called Call by Sharing)
            Means :
            > Function gets reference of the object
            > But not direct access to the variable

In Python:

1️⃣ Arguments are passed as object references

2️⃣ If the object is immutable:

You cannot change it

Any “change” creates a new object

So original is unaffected

3️⃣ If the object is mutable:

You can modify it in place

So original is affected

4️⃣ If you use =:

A new object is created

Reference is changed

Original is not affected


With Examples
Immutable → New Object
def f(x):
    x = x + 1   # new object

a = 5
f(a)
print(a)  # 5


x → new object
a → same old object

Mutable → Same Object
def f(lst):
    lst.append(5)

x = [1,2]
f(x)
print(x)  # [1,2,5]


Same object modified ✅

Mutable + Assignment → New Object
def f(lst):
    lst = [9,9]

x = [1,2]
f(x)
print(x)  # [1,2]


New list created ❌
Old unchanged


In short :
Python uses pass by object reference.
For immutable objects, modifications create new objects.
For mutable objects, in-place changes affect the original.
Assignment always creates a new reference.

"""
"""

Expression Execution
Taking input from user 
Conditional Statements
String Functions
List
Tuples
Dictionaries
sets
while loop 
for loops
Functions
Recursion
-> Factorial

OOPS:
class & objects 
constructor
self keyword
class & Instance Attribute

syntax:

class Class_name:
    Data Members
    Member Function

    //constructor
    def __int__(self):
        //Defination

objects

object=Class_name()

constructor:
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

del keyword
-> del keyword is used to delete object or perticular property of object.

Inheritance
-> Parent class can Inherite properties from Derived class.
-> Types 
1) Single
2) Multiple
3) Multilevel

Super method
-> super() method is used to access methods of the parent class.
-> When we are talking about super keyword It's means we are talking about parent class

class method
-> A class method is bound to the class & receives the class as an implicit first argument.
-> Note - static method can't access or modify class state & generally for utility

Decorator:
-> There are 3 types of decorator.
-> 1) Staticmethod
-> 2) classmethod
-> 3) property

"""


# Conditional Statements
# String Functions
# List
# Tuples
# Dictionaries
# sets

# conditional statements

# if elif else

# a=int(input("Enter the Number: "))
# if(a>=18):
#     print("You Can Vote")
# elif(a<18):
#     print("You Can't Vote")
# else:
#     print("Age Is Not Input")


#  String Functions
str="Suraj"

# Indexing & Slicing

print(str)
print(str[0])
print(str[0:4])
print(str[:5])
print(str[2:])
print(str[-5:]) # Suraj
print(str[-3:-2]) # r
print(str[:-3]) # Su

for i in str:
    print(i)

# 1.
str1=str.endswith("aj")
print(str1)

# 2
str1=str.count("a")
print(str1)

# 3
str1=str.upper()
print(str1)

# 4
str1=len(str)
print(str1)

# 5
str1=str.lower()
print(str1)

# 6

# List

list=[1,2,3,4,5]
print("list with end")
for i in list:
    print(i,end=" ")

print(" ")
i=4
while(i<len(list)):
    print(list[i])
    i-=1
    if(i<0):
        break


print(" ")
print("List")
# Indexing Slicing and Methods :

print(list[2:])
print(list[:5])
print(list[2:])
print(list[-5:])
print(list[:-2])

list.append(10)
print(list)

list.pop(2)
print("After pop",list)


# list[6]=12
# print(list)
#  Methods

tup=(1,2,3,4,5)
print(type(tup))

print(tup)

# Slicing and Indexing

print(tup[1:]) # 2,3,4,5
print(tup[:5]) # 1 2 3 4 5
print(tup[:-3]) # 1 2
print(tup[-3:]) # 3 4 5

"Methods"
print(tup)


dict={
    "name":"suraj",
    "age":10
}

print(type(dict))
print("Keys in dict: ",dict.keys())
print("values in dict: ",dict.values())
print("items in dict: ",dict.items())
print(dict["name"])
dict["gender"]="Male"
print(dict)



sets={1,2,2,3,4}
print(sets)




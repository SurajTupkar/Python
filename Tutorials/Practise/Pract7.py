"""
string
list
tuple
dictionary
set

IO
oops
Classes & objects
constructor
class and instance attributes
Methods
Static Methods


"""

str="Suraj"

print(str) # suraj

print(str[0]) # S
print(str[0:]) #Suraj
print(str[:5]) #Suraj
print(str[1:3]) #ur

print(str[-5:-1]) #Sura
print(str[-5:])  #Suraj
print(str[:-2])  #Sur


for i in str:
    print(i)

print("With While")
i=0
while(i<len(str)):
    print(str[i])
    i+=1


# Methods of string
print("**************************")
print("List")
print(" ")

list=[1,2,3,4,5]

# i=0
for i in list:
    print(list[i-1])

print(list)
print(list[1:]) # 2 3 4 5
print(list[:5]) # 12345
print(list[2:4]) # 34
print(list[-5:]) #12345
print(list[:-1]) #1234
print(list[-4:-2]) #23

# list methods
print("**************")
# tuple
print(" ")

tup=(1,2,3,4)
print(tup)

for i in tup:
    print(i)

print(tup[0])
print(tup[1:]) # 234
print(tup[:3]) #123
print(tup[0:3]) #123
print(tup[-5:]) #1234
print(tup[:-1]) #123

# Methods



"""
IO
oops
Classes & objects
constructor
class and instance attributes
Methods
Static Methods

"""


print("")


# oops

class Student:

    @staticmethod
    def fun():
        print("This is class instance")

    def fun1(self):
        print("This is object instance")

    # default,para ... constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("This is constructor")

    
obj=Student("suraj",24)
print(obj.name)
print(obj.age)

obj1=Student("x",1)
obj1.fun1()

Student.fun()
obj.fun1()







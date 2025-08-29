"""
variable -> containers to store the value.
Data Types -> Python is implicitly typed langugae.
There are 2 types of languaga -> Implicit and Explicit 
Implicit -> You don't need to tell data type of any variable -> Python,Js
Explicit -> You should be mentioned data type while creating varibles -> C,CPP,Java
Comments -> There are 2 Ways to do comments in pythons
# -> Single line comment
""""""" -> MultiLine Comment

Data Types : built in : int,string,boolean,float
             built in : list, tuple, dictionaries & sets

String 

"""

# variable : var is a variable name to store value 10
var=10 
print(var)

# string

str1="string"
print(str1)

# indexing

print(str1[0])

#slicing

print(str1[1:4])
print(str1[1:])
print(str1[:4])
print(str1[-3:])
print(str1[:-1])
print(str1[-6:-1])
print(".......................")

# Methods
print("Methods")

# 1. endswith
str2=str1.endswith("ng")
print(str1.endswith("ng"))
print(str2)

# 2. Capitalize : will make first character of string Capital
print(str1.capitalize())

# 3. replace
print(str1.replace("str","mri"))
print("Replace:",str1.replace("gdhsb","hdcbj"),sep="")

# 4. find : index of first occurence
print("find:",str1.find("tr"),sep="")

# 5. count
print("count:",str1.count('t'),sep="")



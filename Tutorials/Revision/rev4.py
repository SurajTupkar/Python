""" 
Strings : String is data type that stores a sequence of character.
"""

# Ecscape sequence character.
# \n for next line
# \t for tab space

str ="This is a string created in \nthe python language" # the python language print in the next line
print(str)

# Basic Operations

# 1.concatenation

str1="hello"
str2="world"
print(str1+" "+str2)

# length

print(len(str1))
print(len(str2))

# Indexing

str = "This is a String"
""" 
indexing start from 0
so 
T h i s   i s   a    S t r i  n  g
0 1 2 3 4 5 6 7 8 9 10 11 12  13 14

How to acces them using indexing
str[0] -> T
str[1] -> h
str[4] ->    empty space

"""

print(str[5]) # i

"""
Slicing
Accessing parts of a string

str[starting_idx:ending_idx] #ending idx is not included 
"""

str = "This is a String"

print(str[1:6]) #his i
print(str[:4]) #This
print(str[1:]) # his is a String

"""
Slicing
Negative Indexing

str="Negative"

indexing

 N  e  g  a  t  i   v   e
-8 -7 -6 -5 -4 -3  -2  -1

"""

str = "Negative"
print(str[-6:-2]) # gati
print(str[-6:])   # gative
print(str[:-1])   # Negativ
print(str[::-1])  # evitageN





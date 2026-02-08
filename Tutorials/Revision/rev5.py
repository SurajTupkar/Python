# String Functions

# 1.endswith()   : return true if string ends with substr
# 2.startswith() : return true if string starts with substr
# 3.capitalize() : capitalize 1st char
# 4.replace()    : replaces all occurences of old with new
# 5.find()       : returns 1st index of 1st occurence
# 6.count()      : counts the occurence of substr in string
# 7.upper()      : convert string to uppercase
# 8.lower()      : convert string to lowercase
# 9.len(str)     : print the length of string


str = "engineering"

print(str.endswith("ng")) #True
print(str.startswith("Eng")) #True
print(str.startswith("dng")) #False
print(str.capitalize()) #Engineering
print(str[2].capitalize()) #G
print(str.replace("eng","gne"))
print(str.find('e'))
print("count:",str.count('ring'))
print("Upper:",str.upper())
print("Lower:",str.lower())
print(str)
print(len(str))


"""
Q.Why strings are immutable?
-> Strings are immutable because many variables can point to the same string in memory.
If Python allowed changing it, it could affect other variables.
So Python never modifies a string.
Instead, it creates a new string and you must reassign it.

"""
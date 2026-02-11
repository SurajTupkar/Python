# String Functions
"""
 1.endswith()   : return true if string ends with substr
 2.startswith() : return true if string starts with substr
 3.capitalize() : capitalize 1st char
 4.replace()    : replaces all occurences of old with new
 5.find()       : returns 1st index of 1st occurence
 6.count()      : counts the occurence of substr in string
 7.upper()      : convert string to uppercase
 8.lower()      : convert string to lowercase
 9.len(str)     : print the length of string
 10.isalpha()   : check only letters
                  isapha returns True only if:
                  character is letter(a-z or A-Z)
                  No numbers
                  No spaces
                  No special symbols
11.isdigit()    : Only numbers check
12.isalnum()    : Letters and numbers
13.isspace()    : Checks whether all characters are spaces
                  Returns True only if string contains only whitespace
                  If even one letter/number is present → False
14.sorted()     : arranges elements in order and returns a new list.
15.split()      : It breaks a string into parts and returns a list.
                  string.split(separator)
16.join()       : It joins list elements into one string using a separator.
                  Syntax : separator.join(list)


                
"""
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


# Join

# Basic

words = ["A","B","C","D"]
result = " ".join(words)
result1 = "".join(words)
print("with space",result)
print("without space",result1)

# Medium

row = ["101","Rahul","50000","IT"]
csv_line = ",".join(row)
print(csv_line)

# High

record = "2026|Mumbai|50000"
result2 = record.split("|") # string -> List
print(result2)
print("String:"," ".join(result2))


"""
Q.Why strings are immutable?
-> Strings are immutable because many variables can point to the same string in memory.
If Python allowed changing it, it could affect other variables.
So Python never modifies a string.
Instead, it creates a new string and you must reassign it.

"""










"""
SUMMARY:
✅ Indexing / Slicing
✅ upper(), lower()
✅ isalpha(), isdigit()
✅ find(), count()
✅ replace(), strip()
✅ split(), join()
✅ sorted()
✅ Loop on string
✅ Immutability concept

1. String Basics : Creating string
                   Indexing
                   Slicing

s="python"
s[0]      #p
s[-1]     #n
s[1:4]    #yth
s[::-1]   #nohtyp


2. Important String Methods
Case Methods
s.upper()
s.lower()
s.capitalize()
s.title()

Check Methods (Validation - DE Use )
s.isalpha()    # only letters
s.isdigit()    # only numbers
s.isalnum()    # letters+numbers
s.isspace()    # spaces

Search Methods
s.find("a")     # index or -1
s.count("a")    # frequency

Replace & Remove
s.replace("a","@")
s.strip()       # remove spaces
s.lstrip()
s.rstrip()

Split & Join (Very Important for DE)
s.split()       # string → list
" ".join(list)  # list → string

Example:
"hi hello".split()   # ['hi','hello']


3. Looping on String
for ch in s:
    print(ch)


Used in:
✔ Counting
✔ Cleaning
✔ Validation


4. Sorting String
sorted(s)

Used in:
✔ Anagram
✔ Comparison

5. String + Conditions 

Example:

if ch.isalpha():
if ch in "aeiou":


6. Immutability (Concept)
👉 String cannot change in place
👉 Always new copy created

Example:

s = "hi"
s = s.replace("h","b")



"""
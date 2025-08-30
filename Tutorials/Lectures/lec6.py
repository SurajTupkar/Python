# String Functions

str="i am a coder"
str1=False
if(str.endswith("er")):
    str1=True
else:
    str1
    
print("Value of str1:",str1,sep="")

# print(str.endswith("er"))

print(" ")
print("..................")
print("String Funtions")
print(" ")

# 1.endswith("str") -> returns true if string ends with input string.
print("Result of endswith:",str.endswith("er"),sep="")
print("Result of endswith:",str.endswith("en"),sep="")

# 2. capitalize() -> Capitalize first character of string

print("Capitalize:",str.capitalize(),sep="")

# 3 str.replace()
print(str.replace(" co"," ceo"))
print(str)

# 4.str.find() -> find the first occurence of character/string in the given string and give index as a output.

print(str.find("am"))
print(str.find(" "))
print(str.find("i"))
print(str.find("c"))
print(str.find("coder"))

# 5. stri.count()

print(str.count("am"))
print(str.count("a"))

# 6. strip : remove spaces/characters from both side of string
str1="###Hello "
print("strip:",str1.strip("#"),sep="")


# 7. lstrip : remove spaces/characters from left side of string.
str2="*****Hello"
print("lstrip:",str2.strip("*"),sep="")

# 8. rstrip : remove spaces/characters from right side of string.
str2="Hello*******" 
print("rstrip:",str2.rstrip("*"))

# 9. lower()
str3="HELLO"
print(str3.lower())

# 10 upper() : Making uppercase all the letters present in the string
str4="hello world"
print(str4.upper())

# 11 title() : Making first character 
print(str4.title())

# 12 split(delimiter) and join(iterable)
str5="Hello I am DE"
print(str5.split())

print(str5.split())

# 13 join(iterable)
words = ["data","engineering"]
print(" ".join(words))

# 14 endswith()
file="datafile.csv"
print(file.endswith(".csv"))

# 15 startswith()
print(file.startswith(" "))

"""
16.
format() / f-strings
What it does: String formatting.
Use Case: Creating dynamic SQL queries, logs, or filenames.
"""

print(f"{str5} is a")

"""
17
zfill(width)
What it does: Pads number with leading zeros.
Use Case: Standardizing IDs.
"""
num="45"
print(num.zfill(5))


"""
18
isdigit(), isalpha(), isalnum(), isspace()
What it does: Checks string type.
Use Case: Data validation before transformation/loading.

"""

num1="89"
print(num1.isdigit())  # True if num is digit

num2="isabc"
print(num2.isalpha()) # True if num2 is string

num3="is123"
print(num3.isalnum()) # True if num3 is string & num







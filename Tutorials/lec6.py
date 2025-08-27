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

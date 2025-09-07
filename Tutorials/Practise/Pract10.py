"""
string
-> concatination
-> length
-> Indexing


"""

str="Hello"
str1="World"
str3=str+" "+str1
print(str3)
print(len(str))
print(len(str1))
print(len(str3))

# Indexing
print(str[0])

#Types 1: Positive Indexing
print(str[0:1])
print(str[0:4])
print(str[:5]) #Hello
print(str[2:]) #ll0
print(str[::1])

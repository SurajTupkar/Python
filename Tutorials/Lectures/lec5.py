# string


a="2"
b=2.5
print(int(a)+b)

str="This is long"  \
" long string"

print(len(str))
print(str[4])

print(".......................................")

# slicing
print("........... Slicing ............")
print(" ")
print("Positive Indexing")

str1="Hello"
print("str[1] is: ",str1[1],sep="")
print("str[1:4] is: ",str1[1:4],sep="")
print("str[:4] is same as str[0:4] is: ",str1[:4],sep="")
print("str[1] is same as str[1:len(str)] is: ",str1[1:],sep="") # ello

print(" ")

print("Negative Indexing")

"""
 H   E   L   L   O
-5  -4  -3  -2  -1

"""
str2="HELLO"
print(str2[-4:-1]) 
print(str2[:-1])
print(str2[-5:])
print(str2[-1])
print(str2[-5])

print(".......................................")


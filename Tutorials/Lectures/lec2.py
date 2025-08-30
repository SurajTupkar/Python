# Taking input from user 



data=0
print("Taking input from user: ")
data=input()
print("data:",data,sep="")
print("........................................")


"""
-> sep means separator.
-> When you give multiple things to print(), Python will put something between them.
-> By default, that "something" is a space " ".
-> sep = what to put between items in print().
-> Default = space " "

"""

print("printing data using separator:",data, sep="")
print("printing data using separator with hyphen:",data,sep="-")

"""
For Removing Space +(concatination operator) is also used, but it's only work with string value.

"""
print("data:"+data)


print("........................................")


# 1. Taking String input 

data=input("Data: ")
print("Taking String Input From User:",data,sep="")
print("........................................")

# 2. Taking integer input

age=int(input("Input age:"))
print("Age is:",age,sep="")
print("........................................")

# 3. Taking float input 

rating=float(input("Input Rating:"))
print("rating: ",rating)
print("........................................")
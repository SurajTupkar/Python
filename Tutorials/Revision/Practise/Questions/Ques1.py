# Q1. Positive / Negative / Zero
# Write a program to check if a number is:
# Positive
# Negative
# Zero

# num = int(input("Enter a number:"))
# if(num>0):
#     print(f"{num}:is positive")
# elif num<0:
#     print(f"{num}:is negative")
# else:
#     print(f"{num}:is zero")




# Q2. Even or Odd
# Take a number from user and print:
# "Even" if divisible by 2
# "Odd" otherwise


# num = int(input("Enter a number:"))
# if num%2==0:
#     print(f"{num} is a Even number")
# else:
#     print(f"{num} is a Odd number")



# Q3. Pass or Fail
# Input marks (0–100)
# Print:
# "Pass" if ≥ 40
# "Fail" if < 40


# num = int(input("Enter a Marks:"))
# if num>=40 and num<=100:
#     print("Pass")
# elif(num<40 and num>=0):
#     print("Fail")
# else:
#     print("Invalid Marks")


# Q9. Electricity Bill

# Input units consumed.
# Units	Price
# ≤100	₹5/unit
# 101–200	₹7/unit
# >200	₹10/unit
# Calculate total bill.


# units = int(input("Enter units consumed"))

# if(units<=100):
#     bill = units*5
# elif units>100 and units<=200:
#     remain=units-100
#     bill = (100*5) + (remain*7)
# elif units>200:
#     remain = units-200
#     bill = (100*5)+(100*7)+(remain*10)

# print(bill)

# WAP to check if a number entered by the user is odd or even

num1 = int(input("Enter a number1:"))
num2 = int(input("Enter a number2:"))
num3 = int(input("Enter a number3:"))



# if(num%2==0):
#     print("odd")
# else:
#     print("Even")

# WAP to find the greatest of 3 numbers entered by the user.


# if(num1>num2 and num1>num3):
#     print("num is greatest")
# elif num2>num1 and num2>num3:
#     print("num2 is greatest")
# elif num1==num2==num3:
#     print("all are same")
# else:
#     print("num3 is greatest")


# WAP to check if a number is a multiple of 7 or not

if(num1%7==0):
    print("num1 is multiple of 7")
else:
    print("num1 is not multiple of 7")


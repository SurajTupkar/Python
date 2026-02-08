# Taking input from user

# string
# name = input("Enter you name: ")
# print("name:",name)

# # int
# age=int(input("Enter your age: "))
# print("age:",age)

# # float
# price = float(input("Enter price of item:"))
# print("price:",price)

# # boolean
# flag = bool(input("Enter flag:True/False:"))
# print("flag:",flag)

# Conditional Statement

# Q1. Positive / Negative / Zero
# Write a program to check if a number is:
# Positive
# Negative
# Zero

# num = int(input("Enter a Number:"))

# if(num>0):
#     print(num,":is a positive number")
# elif(num==0):
#     print(num,":is a 0")
# else:
#     print(num,":is a Negative Number")



# Q2. Even or Odd

# Take a number from user and print:
# "Even" if divisible by 2
# "Odd" otherwise

# num = int(input("Enter a number:"))

# if(num%2==0):
#     print(num,"is Even Number")
# else:
#     print(num,"is Odd Number")



# Q3. Pass or Fail
# Input marks (0–100)
# Print:
# "Pass" if ≥ 40
# "Fail" if < 40

# marks = int(input("Enter Marks:"))
# if(marks>=40 and marks<=100):
#     print("Pass")
# elif(marks>=0 and marks<=39):
#     print("Fail")
# else:
#     print("Student May be Absent or Enter Invalid Marks")


# Q4. Largest of Three Numbers

# Input 3 numbers.
# Print the largest one.

# num1 = int(input("Enter num1:"))
# num2 = int(input("Enter num2:"))
# num3 = int(input("Enter num3:"))

# if(num1>num2 and num1>num3):
#     print("num1 is greatest")
# elif(num2>num1 and num2>num3):
#     print("num2 is greatest")
# elif(num1==num2==num3):
#     print("all numbers are same")
# else:
#     print("num3 is greatest")


# Q5. Vowel or Consonant
# Input a character.
# Print:
# "Vowel" if a,e,i,o,u
# "Consonant" otherwise
# (Handle uppercase also)

# ch = input("Enter a character:")

# if len(ch) !=1:
#     print("Enter a character only")
# elif ch.isdigit():
#     print("You Enter number")
# elif ch.lower() in ["a","e","i","o","u"]:
#     print("vowels")
# else:
#     print("consonants")



# Grade System

# Input marks.

# Marks	Grade
# ≥ 90	A
# ≥ 75	B
# ≥ 60	C
# ≥ 40	D
# < 40	Fail


# marks = int(input("Enter your marks:"))
# if(marks>=90 and marks<=100):
#     print("A")
# elif(marks>=75 and marks<90):
#     print("B")
# elif(marks>=60 and marks<75):
#     print("C")
# elif(marks>=40 and marks<60):
#     print("D")
# elif(marks<40 and marks>=0):
#     print("Fail")
# else:
#     print("Enter Invalid Marks/Student May be Absent")



# Q7. Valid Age Check
# Input age.
# Print:
# "Child" if < 13
# "Teen" if 13–19
# "Adult" if ≥ 20
# "Invalid" if ≤ 0

# age = int(input("Enter age:"))
# if age<13 and age>=0:
#     print("Child")
# elif age in [13,14,15,16,17,18,19]:
#     print("Teen")
# elif age>=20:
#     print("Adult")
# else:
#     print("Invalid")




# Q8. Leap Year
# Input a year.
# Check if it is leap year.
# Rule:
# Divisible by 4
# But not by 100
# Unless divisible by 400



# year = int(input("Enter a year:"))

# if(year%4==0 and year%100 !=0 or year%400==0):
#     print("Leap Year")
# else:
#     print("Normal Year")



# Q9. Electricity Bill
# Input units consumed.
# Units	Price
# ≤100	₹5/unit
# 101–200	₹7/unit
# >200	₹10/unit
# Calculate total bill.

# unit = int(input("Enter unit:"))
# if(unit<=100 and unit>0):
#     price = 5*unit
#     print("Total Bill:",price)
# elif(unit>100 and unit<=200):
#     price = 7*unit
#     print("Total Bill:",price)
# else:
#     price = 10*unit
#     print("Total Bill:",price)




# Q10. Login System
# Input:
# username
# password
# Correct:

# username = "admin"
# password = "1234"


# Rules:
# If both correct → "Login Successful"
# If username wrong → "Invalid Username"
# If password wrong → "Invalid Password"

username = input("Enter a username:")
password = input("Enter a password:")

if(username=="admin" and password == "1234"):
    print("Login")
elif(username !="admin"):
    print("Enter correct username")
else:
    print("Enter correct password")

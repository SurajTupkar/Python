# Q1. Even or Odd
# Write a program to check whether a number entered by the user is even or odd.

number=int(input("Enter a number:"))
if(number %2 == 0):
    print(number,":is a even number")
else:
    print(number,":is a odd number")


# Q2. Largest of Three Numbers
# Take three numbers as input and print the largest number using if-elif-else.

list=[]

num=int(input("Enter a number1:"))
num1=int(input("Enter a number2:"))
num2=int(input("Enter a number3:"))

if(num>num1 and num>num2):
    print(num,"is greater")
elif(num1>num and num1>num2):
    print(num1,"is greater")
else:
    print(num2,"is greater")


# Q3. Grade System
# A student’s marks are entered. Print grade according to marks:

# 90–100 → A
# 75–89 → B
# 50–74 → C
# Below 50 → Fail

phy=int(input("Enter a marks of phy"))

if(phy>90 and phy<=100):
    print("A")
elif(phy>75 and phy<=90):
    print("B")
elif(phy>50 and phy<=75):
    print("C")
else:
    print("Fail")


# Q4. Leap Year Checker
# Write a program to check whether a given year is a leap year or not.

year=int(input("Enter a year"))
if(year %400 ==0 and year %4==0):
    print("Leap year")


# Q5. Vowel or Consonant
# Take a single character as input and check whether it is a vowel or consonant.

ch=input("Enter a character")
if(ch=="a" or ch=="A" or ch=="E" or ch=="e" or ch=="i" or ch=="i" or ch=="O" or ch=="o" or ch=="U" or ch=="u"):
    print("vowel")
else:
    print("Consonant")
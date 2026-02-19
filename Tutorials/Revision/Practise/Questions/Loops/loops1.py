# # 1. print numbers from 1 to 100

# i=1
# while(i<=100):
#     print(i)
#     i+=1

# # 2. Print numbers from 100 to 1

# i=100
# while(i>=1):
#     print(i)
#     i-=1

# # 3. print the multiplication table of number n

# n = int(input("Enter a number"))

# while(i<=10):
#     print(i*n)
#     i+=1

# # 4. print the elements of the following list using a loop
# lst = [1,4,9,16,25,36,49,64,81,100]
# print(len(lst))
# i=0
# while(i!=len(lst)):
#     print(lst[i])
#     i+=1


# # 5. Search for a number x in this tuple using loop:
# tup = (1,4,9,16,25,36,49,64,81,100)
# x = int(input("Enter a value of x"))
# i=0
# while(i<len(tup)):
#     if(tup[i] == x):
#         print(f"{x} is present in the tuple")
#         break
#     # print(tup[i])
#     i+=1


# 6. Print only numbers divisible by 3 and 5 between 1 to 100 using while loop.

# num = int(input("Enter a value"))
# i =1
# while(i<=100):
#     if(i%3==0 and i%5==0):
#         print(i)
#     i+=1


# 7. Print this pattern using while loop:

# *
# **
# ***
# ****
# *****

# i=1

# while(i<=5):
#     print(i*"*")
#     i+=1


# 8. Print this using while loop:

# *****
# ****
# ***
# **
# *


# i=5
# while(i>=1):
#     print(i*"*")
#     i-=1


# 9. Print this using while loop:

#     *
#    **
#   ***
#  ****
# *****

# i=1
# space=0
# while(i<=5):
#     space = 5-i
#     print(space*" "+i*"*")
#     i+=1

# 10.
# *****
#  ****
#   ***
#    **
#     *

i = 5
space = 0
while(i>=1):
    space = 5-i
    print(space*" "+i*"*")
    i-=1

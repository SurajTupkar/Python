# Q1 Print numbers from 1 to 10
# 1 2 3 4 5 6 7 8 9 10

for i in range(1,11):
    print(i)

# Q2 Print even numbers from 1 to 20
# Output:
# 2 4 6 8 10 12 14 16 18 20

for i in range(2,21,2):
    print(i)

# Q3 Print table of 7
# Output:
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70

for i in range(1,11):
    print(7*i)

# Q4 Find sum of numbers from 1 to 50
# Output:
Sum = 1275
sum=0
for i in range(1,51):
    sum+=i
print(sum)


# Q5 Print all characters of a string
# Input:
# Python

input="Python"
for ch in input:
    print(ch)


# Output:
# P
# y
# t
# h
# o
# n


# Q6 Count how many vowels in a string

# Input:
# education

# Output:
# Vowels = 5

input = "education"
count=0
for ch in input:
    ch.lower()
    if(ch in "aeiou"):
        count+=1
print(count)



# Q7 Find factorial of a number

# Input:
# 5

# Output:
# 120

fact=1
for i in range(1,6):
    fact=fact*i
print(fact)


# Q8 Reverse a string using for loop

# Input:
# hello

# Output:
# olleh

input = "hello"
lst=[]
for ch in input:
    lst.append(ch)

print(lst)
print(lst[::-1])


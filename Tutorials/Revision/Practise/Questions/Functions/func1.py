# Q1. Basic Return
# Write a function add(a, b) that returns the sum of two numbers.

def add(a,b):
    sum=a+b
    return sum

print(add(2,5))


# Q2. Default Parameter
# Write a function greet(name="Guest") that prints:
# Hello, <name>

# If no name is given, print:
# Hello, Guest


def greet(name="Guest"):
    print("Hello",name)

greet()
greet("Sujay")


# Q3. *args
# Write a function total(*nums) that returns the sum of all numbers passed.

def total(*nums):
    return sum(nums)

print("Sum:",total(1,2,3,4))


# Q4. **kwargs
# Write a function print_info(**data) that prints:
# key = value
# For each item.

def print_info(**data):
    for x,y in data.items():
        print(x,y)
    
print_info(name="Amit",age=25)


# Q5. List Modify (Pass by Object)
# Write a function add_zero(lst) that adds 0 at the end of a list.

# Example:

# x = [1,2]
# add_zero(x)
# print(x)   # [1,2,0]

def add_zero(lst):
    lst.append(0)
    

x = [1,2]
add_zero(x)
print(x)


# Q6. Immutable Example
# Write a function increase(n) that increases n by 5 but does NOT change original variable.

def increase(n):
    n = n+5
    print(n)

x=5
increase(x) #10
print(x) # 5


# Q7. Return Multiple Values
# Write a function calc(a, b) that returns:
# sum
# difference
# product

def cal(a,b):
    sum = a+b
    diff = a-b
    pro = a*b
    return sum,diff,pro

print(cal(5,2))


# Q8. Check Even/Odd
# Write a function is_even(n) that returns True if number is even, else False.


def is_even(n):
    if(n%2==0):
        return True
    else:
        return False

n = int(input("Enter a value"))
print(is_even(n))




# Q9. Safe Division (Try/Except)
# Write a function divide(a, b) that:
# Returns a/b
# If b = 0, return "Cannot divide by zero"

def divide(a,b):
    if(b==0):
        return "cannot divide by zero"
    else:
        return a/b

print(divide(6,0))


def clean_data(data):
    result=[]
    for i in data:
        item = i.strip()

        if(item !=""):
            result.append(item)
        
    return result


data = ["  apple ", " banana", " ", "mango  ", ""]
print(clean_data(data))



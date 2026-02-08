"""
1. Expression Execution
2. Taking input From User
3. Conditional Statements
4. Data Types
5. Strings -> Ecscape Character
           -> Concatenation
           -> length
           -> indexing
           -> Slicing : positive and negative
           -> Functions : 1) endswith
                          2) startswith
                          3) capitalize
                          4) replace
                          5) find
                          6) count
"""

#  Expression Execution

# When we divide 2 interger result will be float
# num1=10
# num2=5
# print("float result:",num1/num2)

# But if we do integer division result will be integer
# print("int result:",num1//num2)


# 2. Taking input From User

# int

# num3=int(input("Enter a number"))
# num4=input("Enter a string")
# num5=float(input("Enter a float value"))
# num6=bool(input("Enter a bool value"))

# print(num3,num4,num5,num6,sep=" ")


# 3. Conditional Statements
# if elif else

# 4. Data Types
# int,str,bool,float,

# strings
"""
 -> Ecscape Character
           -> Concatenation
           -> length
           -> indexing
"""
# \n : for new line
# \t : for space
str = "This is a String"
print(str)
print(len(str))

print(str[0])

# positive 

#   T   h   i   s     i   s       a      s    t     r    i     n    g
#   0   1   2   3  4  5   6   7   8  9  10   11    12    13    14   15
#  -13 -12 -11 -10  -9  -8 -7   -6   -5   -4             -3    -2   -1

# slicing
print(str[1])
print(str[0:4])
print(str[1::]) # his ...
print(str[::3]) # Tss rg
print(str[-3:-1])

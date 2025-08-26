# Expression Execution

# 1.string and numeric values can operate together with *

A,B=2,3
Txt="@"
print(2*Txt*3)

# 2.string and string can operate with +
A,B="2",3
print((A+Txt)*3)
# 222@
print((A*3)+Txt) 

# 3.Numeric values can operate with all arithmetic operators

A,B=2,3
C=4
print(A+B*C)


# 4.Arithmetic expression with integer and float will result in float

A,B=10,5.0
C=A*B
print(C)

# 5. Result of division operator with two integers will be float.

A=10 
B=2
print(A/B)




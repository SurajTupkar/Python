# Recursion

def rec(n):
    if(n==0):
        return
    print(n)
    rec(n-1)

rec(5)

# Factorial
def fact(n):
    fac=1
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

print("Factoral ",fact(5))
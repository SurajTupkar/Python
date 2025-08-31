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


#  Questions 

# Write a recursive function to calculate the sum of first n natural numbers

# 5 4 3 2 1


def nsum(n):
    if(n==0):
        return 0
    return nsum(n-1)+n

print(nsum(10))

# write a recursive function to print all elements in a list.
# Hint : use list & index as parameters

def np(list,idx):
    if(idx==len(list)):
        return 
    print(list[idx])
    np(list,idx+1)


list=["a","b","c","d"]
np(list,0)
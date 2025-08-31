# Functions

def sum(a,b):
    print(a+b)

sum(1,2)

def mul(a,b):
    return a*b

print(mul(1,2))

def cal_avg(a,b,c):
    print(int((a+b+c)/3))

cal_avg(1,2,3)  #2

# print function


print("Hello",end=" ")
print("world")


#  Default Parameters:
print("..............Default Parameters:.................")
def def_para(a,b=2):
    return a+b

print(def_para(1))


# list
print("Questions")
def rllist(a):
    # print(list)
    return len(a)

def relisinsing(b):
    return b

list=[1,2,3,4]
print(rllist(list))

print("relisinsing:",relisinsing(list))


def fact(n):
    fact1=1
    while(n>0):
        fact1*=n
        n-=1
    return fact1

print(fact(5))


n=5
factor=1
for i in range(1,n+1):
    factor*=i
print(factor)
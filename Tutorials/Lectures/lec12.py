# for loops

str="string"
for i in str:
    print(i)


# Questions:

# print the elements of the following list using a loop
print("*********************")
l=[1,4,9,16,25,36,49,64,81,100]
for i in l:
    print(i)





# Search for a number x in this tuple using loop
tup=(1,4,9,16,25,36,49,64,81,100)

for i in tup:
    print(i)
else:
    print("**********************")

# range

seq=range(50)
print(seq[48])

for i in range(2,5,2):
    print(i)

print("EVEN NUMBER: ")
for i in range(2,10,2):
    print(i)

#Practise Questions:

print("**********************")

for i in range(101):
    print(i)
print("**********************")
print("Print Number from 100,1")
for el in range(100,0,-1):
    print(el)

count=int(input("Enter Number for Table"))
for i in range(1,11):
    print(i*count)

# WAP to find the sum of first n numbers(using while)

n=int(input("Enter the Number:"))
i=0
sum=0
while(i<=n):
    sum+=i
    i+=1

print(sum)


# WAP to find the factorial of first n number (using for)
fact=1
for i in range(1,n+1):
    fact*=i
    
print(fact)

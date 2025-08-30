# while loops

# i=0
# while(i<5):
#     print("Hello")
#     i+=1

# Practise Questions

# 1. print numbers from 1 to 100
# i=1
# while(i<=100):
#     print(i)
#     i+=1

# 2. print numbers from 100 to 1

# i=100
# while(i>=1):
#     print(i)
#     i-=1

# 3. print multiplication table of a number n
# 4. print the elements of the following list using loop
# [1,4,9,16,25,36,49,64,81,100]

# search for a number x in this tuple using loop
#  (1,4,9,16,25,36,49,64,81,100)

# n=int(input("Enter number for multiplication table "))
# i=1
# while(i<=10):
#     c=(n*i)
#     print(c)
#     i+=1
print("************************************************")
i=0
num_list=[1,4,9,16,25,36,49,64,81,100]

while(i<len(num_list)):
    print(num_list[i])
    i+=1

print("************************************************")
# search for a number x in this tuple using loop
#  (1,4,9,16,25,36,49,64,81,100)

i=0
empty_tuple=(1,4,9,16,25,36,49,64,81,100)
print("Length of tuple:",len(empty_tuple),sep="")
while(i<len(empty_tuple)):
    print(empty_tuple[i])
    i+=1
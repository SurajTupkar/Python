# if elif else

age = int(input("Enter your age: "))
if(age>=18):
    print("you can vote")
elif(age<17 and age>0):
    print("you can't vote")
else:
    print("Enter wrong value")
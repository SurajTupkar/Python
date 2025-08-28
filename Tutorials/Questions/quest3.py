# List :
 # 1. WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
# movie1=input("Enter Movie Name: ",)
# movie2=input("Enter Movie Name: ",)
# movie3=input("Enter Movie Name: ",)
# list=[movie1,movie2,movie3]
# print(list)

movies=[]
movies.append(input("Enter a movie name:"))
movies.append(input("Enter a movie name:"))
movies.append(input("Enter a movie name:"))
print(movies)


# 2. WAP to check if a list contains a palindrome of elements (Hint.use copy() methods)

list1=[1,2,3,2,1]
print(list1[0:])
print(list1[-5:])

# By using reverse method
if(list1== list1[::-1]):
    print("palindrome")
else:
    print("Not palindrome")

# By using .copy method

list2=list1.copy()
list2.reverse()

if list1==list2:
    print("palindrome")
else:
    print("Not Palindrome")




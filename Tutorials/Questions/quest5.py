# WAP to ask the user to enter names of their 3 favorite movies and store them in a list.

# mov1=input("Enter a mov1")
# mov2=input("Enter a mov2")
# mov3=input("Enter a mov3")

# lst=[]
# # list.append(mov1)
# lst.extend([mov1,mov2,mov3])
# print(lst)


# WAP to check if a list contains a palindrome of elements 

ls=[1,2,3,2,1]
l=ls.copy()
l.reverse()

if(ls==l):
    print("palindrome")
else:
    print("Not Palindrome")

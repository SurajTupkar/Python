# Questions on string

# Reverse a String
# Ek string input lo aur uska reverse print karo.
# Example:
# Input → "python"
# Output → "nohtyp"

# str=input("Enter a string: ")
# # list=[]
# # list=str
# l=len(str)
# for i in range(l):
#     print(str[l-1])
#     l-=1


#Ques1 I tried with below slicing but not printing
#Ques2 How can i print str in one line in for loop
# print(str[6:0])
# print(str[-1:-6])

# 0  1  2  3  4  5
# P  y  t  h  o  n
# -6 -5 -4 -3 -2 -1


# Check Palindrome String
# Ek string check karo ki wo palindrome hai ya nahi (palindrome matlab ulta-pulta ek jaisa).
# Example:
# "madam" → Palindrome
# "hello" → Not Palindrome

# str="madam"
# str1=list(str)
# print(str)
# print(str1)

# if(str==str1):
#     print("p")

# Count Vowels and Consonants
# Ek string input lo aur usme vowels (a, e, i, o, u) aur consonants count karke print karo.

count=0
for i in str:
    if(i=="a" or i=="e" or i=="o" or i=="u"):
        count+=1

print(count)
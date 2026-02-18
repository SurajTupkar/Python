# # Q1. Take a string input and print it in uppercase.
# s = input("Enter a string:")
# print(s.upper())

# # Q2. Take a string and print its length.
# print("Length of string:",len(s))

# # Q3.Print the first and last character of a string.
# print("First Char:",s[0])
# print("Last Char:",s[len(s)-1])

# # Q4. Reverse a string using slicing.
# print(s[::-1])

# # Q5. Count how many times 'a' appears in a string.
# print("a in s:",s.count("a"))

# Q6.Check if a string is palindrome.
# Example: madam → Yes

# s = "madam"
# if s == s[::-1]:
#     print("palindrome")
# else:
#     print("Not Palindrome")

# Q7.Remove all spaces from a string.
s = "This is a string"
print(s.replace(" ",""))


# Q8.Count number of vowels and consonants.

vow=0
con=0

for ch in s:
    ch=ch.lower()
    if ch.isalpha():
        if ch in "aeiou":
            vow+=1
        else:
            con+=1

print(vow)
print(con)

# Q9.Replace all 'a' with '@'.
print(s.replace("a","@"))

# Q10.Find the index of first occurrence of a character.
print(s.find("a"))
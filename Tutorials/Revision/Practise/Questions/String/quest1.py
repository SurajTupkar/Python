# Q1. Take a string input and print it in uppercase.

text = input("Enter a string:")
print("string in uppercase:",text.upper())

# Q2. Take a string and print its length.
length=len(text)
print("Length of str:",len(text))

# Q3.Print the first and last character of a string.

print("First character of str:",text[0])
print("Last character of str:",text[length-1])

# Q4. Reverse a string using slicing.
print("Reverse str:",text[::-1])


# Q5. Count how many times 'a' appears in a string.
print("count of a in str:",text.count('a'))


# Q6.Check if a string is palindrome.
# Example: madam → Yes
text_lower=text.lower()
if(text_lower==text_lower[::-1]):
    print("palindrome")
else:
    print("Not Palindrome")

# Q7.Remove all spaces from a string.
print("Without Spaces:",text.replace(" ",""))



# Q8.Count number of vowels and consonants.
vow=0
con=0
for ch in text_lower:
    if ch.isalpha():
        if ch in "aeiou":
            vow+=1
        else:
            con+=1
print("vowels:",vow)
print("consonants:",con)



# Q9.Replace all 'a' with '@'.
print("replace a with @:",text.replace('a','@'))


# Q10.Find the index of first occurrence of a character.
print("First occurence of a:",text.find('a'))
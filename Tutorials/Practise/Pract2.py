"""

Practice Questions

Q1.
s = " Data Engineering "
Remove extra spaces from both sides and print the result.

Q2.
s = "###Pipeline###"
Remove only the # from both sides.

Q3.
s = "Hello Data Engineering"
Convert the string to uppercase.

Q4.
s = "HELLO DE"
Convert the string to lowercase.

Q5.
s = "Hello,World,Data,Engineer"
Split the string by , and print the list.

Q6.
Take the list ["Data","is","fun"] and join it into one string with spaces " " in between.

Q7.
s = "I am learning DE"
Replace "DE" with "Data Engineering".

Q8.
s = "Python is amazing"
Find the index of "amazing".

Q9.
s = " Cloud and Spark "
Remove only the left-side spaces.

Q10.
s = " Cloud and Spark "

"""

# Q1.Remove extra spaces from both sides and print the result.
# strip(), lstrip(), rstrip()
# split(),join(),upper(),lower(),replace(),find()

s = " Data Engineering "
print(s.strip())

# Q2.Remove only the from both sides.
s = "###Pipeline###"
print(s.strip("#"))


# Q3. Convert the string to uppercase.
s = "Hello Data Engineering"
print(s.upper())


# Q4.Convert the string to lowercase.
s = "HELLO DE"
print(s.lower())



# Q5.Split the string by , and print the list.
s = "Hello,World,Data,Engineer"
print(s.split(","))


# Q6.Take the list ["Data","is","fun"] and join it into one string with spaces " " in between.
list=["Data","is","fun"]
print(" ".join(list))



# Q7.Replace "DE" with "Data Engineering".
s = "I am learning DE"
print(s.replace("DE","Data Engineering"))


# Q8.Find the index of "amazing".
s = "Python is amazing"
print(s.index("amazing"))


# Q9.Remove only the left-side spaces.
s = " Cloud and Spark "
print(s.lstrip())


# Q10. Remove only the right-side spaces.
s = " Cloud and Spark "
print(s.rstrip())


"""
String Practice Questions

Length of a String

str1 = "Data Engineering"
# Q: Find the length of str1


Convert to Uppercase

str2 = "hello world"
# Q: Convert this string to uppercase


Convert to Lowercase

str3 = "PYTHON PROGRAMMING"
# Q: Convert this string to lowercase


Remove Extra Spaces

str4 = "   I like Spark   "
# Q: Remove spaces from the beginning and end


Check Prefix

str5 = "bigdata_spark"
# Q: Check if the string starts with "big"


Check Suffix

str6 = "cloud_storage.csv"
# Q: Check if the string ends with ".csv"


Split a Sentence into Words

str7 = "AWS GCP Azure"
# Q: Split this string into a list of words


Join Words into a String

words = ["data", "engineering", "rocks"]
# Q: Join these words into a string separated by "-"


Replace Substring

str8 = "I love Hadoop"
# Q: Replace "Hadoop" with "Spark"


Count Occurrences of a Character

str9 = "banana"
# Q: Count how many times "a" appears in this string


👉 These cover commonly used string functions:

len()
upper()
lower()
strip()
startswith() / endswith()
split() / join()
replace()
count()

"""


# Length of a String
# Q.11 : Find the length of str1

str1 = "Data Engineering"
print("Length of str1:",len(str1))



# Q.12 : Convert this string to uppercase
str2 = "hello world"
print("string to uppercase:",str2.upper(),sep="")



# Convert to Lowercase
# Q.13: Convert this string to lowercase
str3 = "PYTHON PROGRAMMING"
print(str3.lower())


# Remove Extra Spaces
# Q.14: Remove spaces from the beginning and end

str4 = "   I like Spark   "
print("Remove spaces from the beginning and end:",str4.strip(),sep="")



# Check Prefix
# Q.15: Check if the string starts with "big"
str5 = "bigdata_spark"
print(str5.startswith("big"))


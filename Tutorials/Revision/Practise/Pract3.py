# 2. Taking input From User

# a = int(input("Enter a integer number"))
# print("integer:",a)
# b = input("Enter a string value")
# print("string:",b)
# c = float(input("Enter a float value"))
# print("float:",c)
# d = bool(input("Enter a bool value"))
# print("bool:",d)


# 3. Conditional Statements

# a = int(input("Enter a value"))
# b = int(input("Enter a value"))
# if(a>b):
#     print("a is greater than b")
# elif(a==b):
#     print("a is equal to b")
# else:
#     print("a is less than b")

# 4. Data Types
# int,float,bool,string,list,tuple

# 5. Strings -> Ecscape Character
#            -> Concatenation

# print("Enter a input\nif you are entering\tinteger")

#            -> length
#            -> indexing : positive and negative
#            -> Slicing : positive and negative

# s="Engineering"
# print(len(s))
# print(s[0])   # E
# print(s[1])   # n
# print(s[1:5]) # ngin
# print(s[:6])  # Engine
# print(s[1:])     # ngineering
# print(s[::-1])   # gnireenignE
# print(s[-5:-1])  #    erin

#            -> Functions : 1) endswith
#                           2) startswith
#                           3) capitalize
#                           4) replace
#                           5) find
#                           6) count
                        #   7) upper
                        #   8) lower
                        #   9) len(str)
                        #   10) isalpha()
                        #   11) isdigit()
                        #   12) isalnum()
                        #   13) isspace()
                        #   14) sorted
                        #   15) split
                        #   16) join

s = "Engineering"

print(s.endswith("g"))   #True
print(s.endswith("a"))   #False
print(s.startswith("E")) #True
print(s.startswith("n")) #False
print(s.capitalize())
print(s.replace("En","en"))
print(s.find("e"))
print(s.lower().count("e"))

#                          7) upper
#                          8) lower
#                          9) len(str)
#                          10) isalpha()
#                          11) isdigit()
#                          12) isalnum()
#                          13) isspace()
#                          14) sorted
#                          15) split
#                          16) join

print(s.isalpha()) #True : Check only Letters 
print(s.isdigit()) #False : Check only digit
print(s.isalnum()) # True : Check Letters and numbers
s1=" "
print("space:",s1.isspace())

text = "A,B,C,D"
print(text.split(","))

text1 = "A  B C"
print(text1.split())



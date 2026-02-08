"""
✅ Create list
✅ Indexing / slicing
✅ Mutable concept
✅ append / insert / extend
✅ remove / pop / clear
✅ sort / reverse
✅ Looping
✅ copy concept
✅ Nested list


 list in python
 -> A built in data type that stores set of values.
 -> It can store elements of different types :  int
                                                float
                                                string
                                                boolean
                                                list
                                                tuple
                                                set
                                                dictionary
                                                even functions, objects, etc.

In short : A Python list can store heterogeneous data including primitive types and complex objects.



Q. Why lists are mutable?
Lists are mutable because they are designed to store dynamic data that needs frequent updates. 
This improves performance and usability.
"""

lst =[
    10,                  #int
    3.14,                #float
    "data",              #string
    True,                #boolean
    [1,2,3],             #list
    (4,5),               #tuple
    {"a":1,"b":2}        #dict
]

print(lst)

# How to access elements stored in list

print(lst[0])          #10
print(lst[1])          #3.14
print(lst[2])          #data
print(lst[3])          #True
print(lst[4][0])       #1
print(lst[4][2])       #3
print(lst[5][1])       #5
print(lst[6]["a"])     #1

print("for loop")
for i in range(len(lst)):
    if(i==4):
        print(lst[i])

# list slicing
print("slicing")

marks=[10,20,30,40,50]

print(marks[1:4])   # 20,30,40
print(marks[:5])    # 10,20,30,40,50
print(marks[0:])    # 10,20,30,40,50
print(marks[0:5:3]) # 10,40
print(marks[-5:-1]) # 10 20 30 40 50
print(marks[::-1])  # 50 40 30 20 10

# Modify List Because its Mutable
marks[0] = 100      # [100,20,30,40,50]
print(marks)

# Important List Methods
# 1. Add Elements : append,insert,extend

marks.append(5)      # add 5 at the end
print(marks)         # [100,20,30,40,50,5]

marks.insert(1,99)   # Add at index : 99 add at index 99 
print(marks)         # [100,99,20,30,40,50,5]

marks.extend([7,8])  # add many at the end
print(marks)         # [100,99,20,30,40,50,5,7,8]

# 2. Remove Elements
# remove,pop,pop(index),clear

marks.remove(20)    # remove by value(20)
print(marks)        # [100,99,30,40,50,5,7,8] : Remove 20 from list

marks.pop()         # remove last element from list 
print(marks)        # [100,99,30,40,50,5,7]

marks.pop(2)        # remove element by index
print(marks)        # [100,99,40,50,5,7]

# marks.clear()       # empty list : clear all elements from list
print("Empty List:",marks)        # []

# 3. Search & Count

print(marks.index(99))      # position : Find index of value
print(marks.count("a"))     # Frequency of value


# 4. Sort and Reverse
# sort works only when all elements are same type.
# if i have list of mixed string and int elements Python cannot compare int with string. so it will crash.

lst=[10,40,70,20,80,"d","a","c","e"]  

"""
print(marks.sort()) 

it will crash or getting error like TypeError: '<' not supported between instances of 'str' and 'int'

Sorting Means:
Python compares values:
10<20   This is ok
"a"<"b" This is ok
10<"a"  but this not XXX
because python cannot compares int with string, so it crashes

When .sort() works

case1 : All Numbers
Case2 : All Strings
Case3 : Same Datatype only

"""

#  How to sort mixed list

# Method 1: Separate Numbers and Strings

# nums=[]
# chars=[]

# for i in lst:
#     if(type(i)==int):
#         nums.append(i)
#     else:
#         chars.append(i)

# nums.sort()
# chars.sort()

# print(nums + chars)






nums  = []
chars = []

for i in lst:
    if(type(i)==int):
        nums.append(i)
    else:
        chars.append(i)

nums.sort()
chars.sort()
print(nums + chars)

nums.reverse()
chars.reverse()
print(nums + chars)























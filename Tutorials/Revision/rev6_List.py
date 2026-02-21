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

marks.insert(1,99)   # Add at index : 99 add at index 1 
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


# sort :sort in ascending order

l=[1,8,9,4,7,2]

# if i have to return list in descending order
l.sort(reverse=True)
print("Descending order:",l)

nums.reverse()
chars.reverse()
print(nums + chars)

# 5. loops on list

# Normal Loop

for i in lst:
    print(i)

# Use when index needed.
for i in range(len(lst)):
    print(lst[i])


# 6.Useful Built-in Functions

# len(lst)
print(len(lst)) # 9

# max
# print(max(lst)) # Not supported because list contain mixed data type
print(max(marks)) # 100

# min
print(min(marks)) # 5

# sum
print(sum(marks)) # 301

# 7. Nested List

lst=[[1,2],[3,4],[3,5],[5,7,9]]

print(lst[0][1]) # 2
print(lst[3][2]) # 9

# 8. copy

"""
Why do we need copy list?
Because this is dangerous:
a=[1,2,3]
b=a

Now:
a and b point to same memory.

so:
b[0]=100
print(a) # 100,2,3 
100 replace the value at index 0

we changed b but a also changed.
Why?
Because both refer to same list

This is called : shallow reference (same object)
a ---> [1,2,3]
b ---> [1,2,3]
one list,two names

correct way : copy list(new memory)
we want:
a->[1,2,3]
b->[1,2,3]
Two different list
"""


x=[1,2,3]
z=x

print("x:",x)
print("z:",z)

# below both list will change because both point to same memory location
z[0]=199
print("x:",x)
print("z:",z)

# Method 1: .copy()

a=[[1]]
b=a.copy()

b[0]=100
print("a:",a)
print("b:",b)
print("a:",id(a[0]))
print("b:",id(b[0]))
print("a:",id(a[0]),"b:",id(b[0]))

# Note : .copy creates shallow copy 

"""

.copy() and [:] both create shallow copy.
For normal list, shallow copy behaves like deep copy.
For nested list, it remains shallow.

In short
.copy() and slicing create shallow copy.
For simple lists it behaves like deep copy.
For nested lists we must use deepcopy().


In Python, lists are mutable, but immutable elements like int and string are replaced, not modified.
A shallow copy creates a new outer list but shares references of inner elements.
A deep copy creates completely independent objects.


Immutable → int, str, float, bool, tuple
Mutable   → list, dict, set

list[i]=x → overwrite reference

.copy() / [:] → Shallow copy

Normal list → element references shared
Nested list → inner list shared

deepcopy → full independent copy

id() unreliable for immutable types


"""

# slicing

l=[1,2,3]
m=l[:] # l[start:0,end:len(l),step:1]
print("l:",l)
print("m:",m)
l.append(19)
m.append(30)
print("l:",l)
print("m:",m)
print("l:",id(l[0]))
print("m:",id(m[0]))


# nested list
import copy
ls=[[1,2],[3,7],["a","b"]]
bs=copy.deepcopy(ls)
print("ls",ls)
print("bs",bs)
bs.append(5)
bs[0].append(5)
print("bs:",bs)

"""
Shallow copy copies only references of inner objects, so nested structures are shared. 
Deep copy recursively copies all objects, so no memory is shared.

Shallow Copy:
- .copy(), [:]
- Outer list new
- Inner shared
- Unsafe for nested

Deep Copy:
- copy.deepcopy()
- Everything new
- Safe
- More memory


"""















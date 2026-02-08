"""
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

print(marks[1:4]) # 20,30,40
print(marks[:5])  # 10,20,30,40,50
print(marks[0:])  # 10,20,30,40,50
print(marks[0:5:3]) #10,40
print(marks[-5:-1]) 



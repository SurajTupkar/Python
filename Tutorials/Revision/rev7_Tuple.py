# Tuple

"""
What is Tuple:
                An ordered,immutable collection of elements.
                Means:
                -> Order matters
                -> Indexing allowed
                -> Duplicate allowed
                -> Cannot be changed

Difference: List vs Tuple

Feature   |      List     |     Tuple
Brackets  |       []	  |     ()
Mutable	  |      Yes      |     No
Speed	  |     Slower    |     Faster
Memory	  |      More     |     Less
Change	  |    Allowed    |     Not allowed

"""

# 1. Creating Tuple:
# Normal Tuple

t=(1,2,4)

# without Brackets(packing)

t=1,2,3
print("t",t)

# Single Element Tuple

t1=(10,) # correct Why, Because comma makes tuple
t2=(10)  # wrong -> int

print("t1",type(t1))
print("t2",type(t2))


# 2. Accessing Tuple Elements
print(t[0])
print(t[-1])

# Slicing

print(t[1:3])   # 2,3
print(t[:3])    # 1,2,3
print(t[1:])    # 2,3
print(t[::-1])  # 3,2,1
print(t[-3:-1]) # 1,2
print(t[-3:])   # 1,2,3
print(t[:-1])   # 1,2

# 3. Why Tuple is Immutable?
"""
t[0] = 100
t.append(5)
print(t)

TypeError: 'tuple' object does not support item assignment
"""

"""
# Mutable Inside Tuple
-> tuple itself is immutable,
-> but elements inside can be mutable.
"""
tup=([1,2],[3,4])
tup[0].append(4)
print(tup)

"""
tup=([1,2],[3,4])
tup[0].append(4)
print(tup)
Why?
Because:
Tuple not changed
List inside changed
"""

# 4. Tuple Methods

# count()

tup=(1,2,3,3,3,2,3)
print(tup.count(3))

# Index
print(tup.index(3))

# 5.Looping in Tuple

for i in tup:
    print(i)

# 6. When to use Tuple
"""
Use tuple when:
            -> Data Should not change
            -> Read-only data
            -> Configuration values
            -> Faster iteration
"""

# What is Tuple Packing?
# Packing = putting multiple values into one tuple

tup = 10,20,30
print(t)  # (10,20,30)

# Here :
#       Python automatically packs 10,20,30 into a tuple.
# so 10,20,30 -> (10,20,30)
# This is called tuple packing

# What is Tuple Unpacking
# Unpacking : Taking values out of tuple into variables.

t = (10,20,30)
a,b,c=t

print("a:",a)
print("b:",b)
print("c:",c)

# Tuple values are "unpacked" into variables.
# So,
# (10,20,30) -> a=10,b=20,c=30
# Rule : No.of variables = No.of values

t=(1,2,4)
# a,b=t # Error

# correct
a,b,c=t

# Without packing/unpacking:
a=5
b=10
print("Before Swapping")
print("a:",a,"b:",b)
temp=a
a=b
b=temp
print("After Swapping")
print("a:",a,"b:",b)

a=5
b=10
print("Before Swapping")
print("a:",a,"b:",b)
a,b=b,a
print("After Swapping")
print("a:",a,"b:",b)


"""
How?
Step 1: Packing
(b, a) → (10, 5)

Step 2: Unpacking
a=10, b=5
"""

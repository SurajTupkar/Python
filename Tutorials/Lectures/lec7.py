# List in python

marks=[10,20,30,40,50]
print(len(marks))
print(type(marks))
print(marks[0])
print(marks[1])
# marks[2]=90       # We can modify list : Mutable
print(marks[2])

print(".... Slicing ....")

print(marks[1:4])
print(marks[1:])
print(marks[:5])
print(marks[1])
print(marks[-3:-1])
print(marks[-3:])
print(marks[:-3])


print(".................")
str="HELLO"
print(str[2])

# str[2]="D"      # TypeError: 'str' object does not support item assignment : Because strings are immutable in python

print(str)


print(".................")


print("List Methods")

# 1. append 

list=[1,3,2,9,4]
print(list)
list.append(5)
print("append 5: ",list)
print("....................")

# 2. sort
print("sort method")
list.sort()
print(list)

list.sort(reverse=True)
print(list)
print("....................")

# 3. reverse
list.reverse()
print(list)

# 4. insert element at index

list.insert(2,45)
print(list)

# 5. remove method -> Remove first occurence of element

list.remove(1)
print(list)

# 6. pop -> removes element at idx
list.pop(2)
print(list)


# 7. extend

list1=[1,2,"Ram",7.8]
list1.extend("Suraj")
print(list1)

# 8. insert(index,value)
list1.insert(1,90)
print(list1)
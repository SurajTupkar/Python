"""
Set 
-> Set is the collection of the unordered items.
-> Each element in the set must be unique and immutable.
-> We can store bool,int,float,str,tuple in set but not list and dict because they are immutable. 

IMP Note :
-> Set is Mutable because we can use add(),remove(),pop() methods
-> But the elements in set are immutable
"""

collection = {1,2,2,2,3}
print("Type:",type(collection))
print("Values in collection:",collection) # repeated elements stored only once so it resolved to {1,2,3}


# Why Set is unordered
col = {6,3,1,2,"world","hello"}
print("Unordered:",col)  

"""
set is unordered because it is implemented using hashing (hash table), not indexing
It does not store elements in sequence like list/tuple.

Why Hashing uses for set?
-> Because it makes operations very fast
-> Main goal of set :
                    -> Fast search
                    -> Fast insert
                    -> Fast delete

Example : 
            if 25 in s:
            This is almost O(1) constant time.
            Because hashing is used


IN SHORT :
Set is unordered because it uses hash-based storage,where elements are stored based on their hash values instead of insertion order,to provide fast lookup and uniqueness.
"""


null_set=set()
print(type(null_set))


# Methods in Set :

print("collection:",collection)

# 1.add(element) : To add elements in set
collection.add(30)
print("add 30:",collection)

# 2.len(set)     : Length of set
print("Length:",len(collection))

# 3.remove(element)      : Remove Elements from set
collection.remove(30)
print("After Removing 30:",collection)

# collection.remove(30)  If 30 is not present and we are trying to remove it will give error.
print("30 does not exist:",collection)


# 4.clear()               : To clear set
collection.clear()
print(collection)

# 5.pop : Remove random elements
col.pop()
print("After pop:",col)

s1 = {1,2,3,3,4}
s2 = {1,2,5,6,7,8}

# 6. union : combines both set values and returns new.
print("union:",s1.union(s2))

# 7. intersection : combines common values and returns new.
print("intersection:",s1.intersection(s2))




#  Questions 

"""
Store following word meanings in a python dictionary:
table : "a piece of furniture","list of facts and figures:
cat   : "a small animal"

"""
print("Questions:")
word_mean = {
    "table" : ["a piece of furniture","list of facts and figures"],
    "cat"   : "a small animal" 
   
}

print(word_mean)

set = {"python","java","C++","python","javascript","java","python","java","C++","C"}
print("Required clasroom:",len(set))

math  = int(input("Enter math marks"))
phy   = int(input("Enter phy marks"))
chem  = int(input("Enter chem marks"))

empty_dict={}
print(type(empty_dict))
empty_dict.update({"math":math})
empty_dict.update({"phy":phy})
empty_dict.update({"chem":chem})
print(empty_dict)


values = (9,9.0)
print(values)

val = [9,9.0]
print(val)
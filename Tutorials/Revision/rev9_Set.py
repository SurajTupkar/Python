"""
Set 
-> Set is the collection of the unordered items.
-> Each element in the set must be unique and immutable.
-> We can store bool,int,float,str,tuple in set but not list and dict because they are immutable. 


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


null_set=set({})
print(type(null_set))
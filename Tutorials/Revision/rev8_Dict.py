# Dictionary

"""
-> Dictionaries are used to store data values in key:value pairs
-> They are unordered : Means no indexing like string,list and tuple
-> They are mutable   : values can be changable
-> And Don't allow duplicate keys
-> key must be unique



"""

info = {
    "age":28,          # int
    "price":23.30,     # float
    "is_adult":False,  # bool
    "key":"value",     # string
    "list":[10,20,30], # list
    "tuple":(1,2,3),    # tuple

    # key can be int,float,bool and string but not list and tuple

    12:"XYZ",
    45:956,
    1:45.25,
    2:True,
    3:["A","B","C"],
    4:(1,"A",3,True),

    (1,2,3):"String"


    
}



print(info)
print("Int Value from Dict:",info["age"])              # 28
print("Float value from Dict:",info["price"])          # 23.30
print("Bool value from Dict:",info["is_adult"])        # False
print("String value from Dict:",info["key"])           # value
print("List from Dict:",info["list"])                  # [10,20,30]
print("tuple from Dict:",info["tuple"])                # (1,2,3)
print("First Value from List:",info["list"][0])        # 10
print("First value from tuple:",info["tuple"][0])      # 1

print("Int Key can store string value:",info[12])
print("Int key can store int value:",info[45])
print("Int key can store float value:",info[1])
print("Int key can store bool value:",info[2])
print("Int key can store List:",info[3])
print("Int key can store Tuple:",info[4])


print("Tuple can also store values:",info[(1,2,3)])


#  can change value of exiting key

info["age"]=36
print(info["age"])

# Can add new key & value pair

info["surname"]="VBN"
print(info)

#  can create null Dictionary

null_dict={}
print("null_dict:",null_dict)


# Nested Dictionaries:

student = {
    "name"  : "Anuj",
    "score" : 
    {
        "math" : 95,
        "chem" : 89,
        "phy" : 56
    }
}

print(student)
print("name:",student["name"])
print("score of phy:",student["score"]["phy"])



# Methods in Dictionary :

# 1. len() : To return the length of dict


print(len(info))
print(len(student))


# 2. keys() : To return all keys from dict
print("keys:",student.keys())
print("keys typecast in list:",list(student.keys()))


# 3. values() : To return all values from dict
print("values:",info.values())
print("values cast in list",list(info.values()))

# 4. items : return all (key,val) pairs as tuples
print("Key value pairs using items",info.items())
print("Key value pairs using items",list(info.items()))

# 5. get("key")  : return the value according to key
#                : If key is not present It does not give error (this is the main benefit) 
#                : syntax : dict.get(key,default_value)  # default value is optional



record = info.get("name")
print("get value from key:",record)  # None because name key is not present and default value is not given

record = info.get("name","XYZ")
print("get value from key if key is not exist print default value:",record)


"""
-> get() method returns the value for a given key in a dictionary.If the key does not exist,it returns None or a default value instead of raising an error.


Q. Why we use get method if we can access values with [] ?
-> We use get() instead of [] because get() prevents keyError when a key is missing and allows providing a default value, making code safer and more reliable in production system


"""

# 6.update()

new_dict = student.update({"age":20})
new_dict = student.update({"name":"Anil","salary":56000})
print(student)
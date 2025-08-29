# Dictionaries

dict={
    "name":"XYZ",
    "age" :25,
    "topic":"Dict",
    "is_completed":False,
    "marks":[45,58,65,95],
    "string":("A","B","C","D"),
    12:56,
    (1,2,4):23

}

print(dict)

# how to access perticular key value-pair
print("name:",dict["name"],sep="")

# How to modify/update value of dict
dict["name"]="ABC"

# How to add new value in dict
dict["update"]="updation_add"
print(dict)


# Nested Dictionaries

nes_dict={
    "name":"suraj",
    "subject":{
        "chem":78,
        "phy" :59,
        "math":89
    }
}

print(nes_dict["subject"]["phy"])

print(nes_dict)

print(".........................")

# Methods:

print(".......... Methods ...........")

myDict={
    "name":"XYZ",
    "age" :25,
    "topic":"Dict",
}


# 1. keys : return all keys present in the dictionry

print(myDict.keys())

# 2. values : return all values present in the dictionary

print(myDict.values())

# 3. items : return all (key,val) pairs as tuples

print(myDict.items())

# 4. get("keys") : returns the value according to key

print(myDict.get("age"))

# 5. update(new dict) : Insert the specified items to the dictionary

my_Dict1=myDict.update({"subject":"Math"})
print(myDict)

myDict.update({"subject1":"M2"})
print(myDict)
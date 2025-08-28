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




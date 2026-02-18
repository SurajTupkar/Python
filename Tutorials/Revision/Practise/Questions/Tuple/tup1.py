t = (10,20,30)
print("old tuple:",id(t))
t = t + (40,)
print("new tuple:",id(t))
print(t)

"""
-> Tuples are immutable, but we can create new tuples by concatenation and reassigning the references.
-> Here We are not modifying the old tuple.
-> We are creating a NEW tuple.

"""

# Q2.

t = (1,2,3)
# t[1] = 50
# print(t)

"""
-> When we try to print t its giving error : TypeError : 'tuple' object does not support item assignment.
OR
-> It will give error because tuple is immutable, so we can't modify it.

"""

# Dict

d ={
    "a":10,
    "b":20,
    "c":30
}

print(d)
print(d.get("b"))

# Q2.

d = {"x":5, "y":10}
# print(d["z"])

# Q3

d = {"id":101, "name":"Amit"}
d["name"] = "Rahul"
print(d)

# Q4.

d = {"p":100, "q":200}
print("r:",d.get("r",500))

# Q5.

data = ["a","b","a","c","b","a"]

d={}
for x in data:
    d[x]=d.get(x,0)+1
    print(d)

    
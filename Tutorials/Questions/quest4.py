# Tuple

# WAP to count the number of students with the "A" grade in the following tuple.

tup=("C","D","A","A","B","B","A")
print(tup.count("A"))

print(tup)

# sorted() returns a new list with elements sorted. 
tup1=sorted(tup)
print("tup1",tup1)

# Convert to list → sort → convert back :
tupli=list(tup)
tupli.sort()
print(tupli)

tup3=tuple(tupli)
print(tup3)




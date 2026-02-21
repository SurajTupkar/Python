"""
FILE I/O :
-> Python can used to perform operations on file 
-> Operations like read,write

Types of file :
                1) Text Files : .txt,.docx,.log etc
                2) Binary Files : .mp4,.mov,.png,.jpeg etc
-> When we access both files format by using python they are different.
-> But When they are stored in memory are all bits(0,1)

# Open,read and close file :
-> We have to open file before reading and writing.
-> Syntax :
            file = open("file.name","mode")

-> Common Modes : 

r : Read
w : write(overwrite)
a : append
r+: Read + Write
w+: Write + Read

"""

# Reading Files :

# 1. Read Entire File :

f = open("D:\DE\Python\Tutorials\Lectures\demo.txt","r")
data = f.read()
print(data)

f.close()

# 2. Read Line by Line

f1 = open("D:\DE\Python\Tutorials\Lectures\demo.txt")

for line in f1:
    print(line.strip())

f1.close()

# 3. Read All Lines in List

f2 =  open("D:\DE\Python\Tutorials\Lectures\demo.txt")

lines = f2.readlines()
print(lines)

# writing Files

f3 = open("output.txt","w")
f3.write("Hello DE")
# f3.close()

# w deletes old data

# f3.write("Learning python")
f3 = open("output.txt","r")
data3 = f3.read()
print(data3)


# Append (Add at End)

f4 = open("output.txt","a")
f4.write("New Line Added\n")
# f4.close()

f4 = open("output.txt","r")
data4=f4.read()
print(data4)


# Best Practice: Using with

with open("output.txt","r") as f5:
    for line in f5:
        print(line)

with open("output.txt","r") as f6:
    data6 = f6.readlines()
    print(data6)
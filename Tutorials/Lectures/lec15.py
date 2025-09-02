#  IO File

# 1. Reading File
# read,readline

# f=open("D:\DE\Python\Tutorials\Lectures\demo.txt","r")
# # data=f.read()
# line1=f.readline()
# print(line1)
# line2=f.readline()
# print(line2)
# f.close()

# data=f.write("Overwrite file content using write")
# print(data)



# Writing to a file
"""
modes:
1) w : overwrite a existing file
2) a : append a file at the end 

-> If file is not present ... and we try to open a file that file it's newly created a file
"""

# overwrite
# file=open("D:\DE\Python\Tutorials\Lectures\demo.txt","w")
# data=file.write("I am going to overwrite content from existing file")
# print(data)

# read
# file1=open("D:\DE\Python\Tutorials\Lectures\demo.txt","r")
# readdata=file1.read()
# print(readdata)

#append

# file=open("D:\DE\Python\Tutorials\Lectures\demo.txt","r")
# # data=file.write("\nI am going to append some other text on the next line using back slash n")
# data=file.read()
# print(data)
# file.close()


"""
Mode : r+
-> We can overwrite file using "r+" mode but data write at the begining of the text.
-> then we can read it also
"""

# file=open("D:\DE\Python\Tutorials\Lectures\demo.txt","r+")
# data=file.write("I am writing another text in next line by using r+ mode")
# print(data)
# d1=file.read()
# print(d1)


"""
Mode : w+
Open for reading and writing.
The file is created if it does not exist,otherwise it is truncated.
The stream is positioned at the biginning of the file.

"""

file=open("D:\DE\Python\Tutorials\Lectures\sample.txt","w+")
# data=file.write("This is Sample.txt file")
# print(data)
print(file.read())


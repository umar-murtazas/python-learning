## file handling
f = open("datatypes.py", "r") #refernced f to this data or it points to it, now f can be used to perform anything on this data
print("file discription is printed becuase we didnt read() yet : ", f)
##<_io.TextIOWrapper name='datatypes.py' mode='r' encoding='cp1252'>
### io -> input/output        textiowrapper -> text file handler, opened file in text stream as str.
### encoding -> digit mapping of everything like ASCII, eg 18 -> A    28 -> @
print("text stream : ", type(f.read())) # both of these return the same file discription

b = open("datatypes.py", "rb") # rb -> binary mode, no encoding
print("file discription is printed becuase we didnt read() yet : ", b) 
print("binary stream : ", type(b.read())) # rb -> binary stream, shows data in raw bits, used for videos,images,pdf

# print(f.read())
name = f.read() #pointer will be at the end of the file, nothing new to read
# name = b.read() # for binary stream
print("first read() : ", name)

f.seek(10,2)  # resets the pointer, 0->start, 1->current position, 2->end.
## negative bytes doesnt work on text stream
b.seek(-5,2) # but it works on binary stream, last 5 bytes

name = f.read() # since there is nothing else to read, we get an empty str instead of file data.
# name = b.read() # for binary stream
print("first read() already read everything, hence empty str : ", name)
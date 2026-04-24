## file handling
'''
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

# f.seek(10,2)  # resets the pointer, 0->start, 1->current position, 2->end.   # 2 wouldnt work here its already at the end.
## negative bytes doesnt work on text stream
b.seek(-5,2) # but it works on binary stream, last 5 bytes

# name = f.read() # since there is nothing else to read, we get an empty str instead of file data.
name = b.read() # for binary stream
print("first read() already read everything, hence empty str : ", name)

'''
f = open("datatypes.py", "r")
print(f.read(11)) # first 11 characters

r = open("sample.txt", "r")
print(r.readline()) # reads one line at a time
print(r.readline()) # reads second line
print(r.readline()) # reads third line
print(r.readlines()) # reads all lines into a list

# for line in f:
#     print(line) # first 11 charcters wouldnt be shown becuase of the above read()

# w = open("sample.txt", "w") #overwrites existing data
# w.write("this is hte new sample data that has been updated inside the file")
# w.close()
# a = open("sample.txt", "a") # modifies the data.
# a.write("\nthis is another line that has been added into the file by appending")
# a.close()
with open("sample.txt", "r") as changed: #auto closes file
    f = changed.read()
    print(f)

file = open("sample.txt", "r")
for line in file: #each line already has \n and print adds another one.
    # line.strip() # creates copy of the original data since str are immmutable
    l = line.strip()
    print(l) # now the extra spaces will be removed


print(file.tell()) # shows th current file pointer position in bytes
file.seek(12,0) 
print(file.tell())

import os
if os.path.exists("sample.txt"): #finds if the file exists or not
    print("exists")
# 😒
# with open("img.jpg", "b") as a:
#     print(a.read())

# ---------------reading from csv and json files.-------------------
import csv
with  open("sample.txt", "r") as f:
    reader = csv.reader(f) #reads line by line and converts it into a list
    next(reader) # moves one step forward, skips one row
    for row in reader:
        if len(row) != 3: #skips invalid entries
            continue
        else:
            print(row)
    print("row one : ", row[0]) # gives data of one column
# 😒 needs refactoring
    f.seek(0)
    dictreader = csv.DictReader(f, fieldnames=["name", "age", "job"])
    next(f)
    next(f)
    next(f)
    for d in dictreader:
        # if not all(d.values()): # all() returns true if every value is true
        if len(d) != 3:
            continue # does nothing on the current iteration
        print(d)

l = [10, 20, 30, 40]
it = iter(l) # converts list from an iterable to iterator, files are auto converted into a 
next(it) # skips the first element
for i in it:
    print(i)

ports = [21, 53, 56, 80, 443]
with open("portdata", "w", newline="") as w: #newline to prevent extra lines
    # write = csv.writer(w) # writes to a file
    # write.writerow(["Port", "status"]) # writes one row into the file.
    # for p in ports:
    #     write.writerow([p, "open"])
    write = csv.DictWriter(w, fieldnames=["port", "status"])
    write.writerow({"port": 21, "status": "open"})
    write.writerow({"port": 80, "status": "open"})
    write.writerow({"port": 53, "status": "open"})
    write.writerow({"port": 443, "status": "open"})

import json
var = {
    "name": "ahmed",
    "class": 3,
    "age": 12
}
data = []
for i in range(10):
    data.append(var)
with open("work.json", "w") as j:
    json.dump(data,j, indent=4)  # enter data into the file
    
with open("work.json", "r") as l:
    access = json.load(l) # read data form the file
    print(access[0]["name"])
    # print(json.loads("work.json"))

json_str = json.dumps(data) # converts python data into a json text
print(type(json_str)) # py = {"name":"ali"} + text = '{"name":"ali"}'
python_obj = json.loads(json_str) # converts json text into python object
print(type(python_obj)) # str -> list/tuple/dict

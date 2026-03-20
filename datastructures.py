#list -> mutable, ordered
mylist = [10, 20, 30, 40]
print("0 access the 1st element : ", mylist[0])
print("-1 access the elemnts from the end : ", mylist[-1]) # negative indexing
mylist[2] = 32 # mutablity, values can be changed afterwards
print("modified : ", mylist)

print("appended : ",  mylist.append(50)) # adds element at the end, prints None becuase they dont return anything
print("removed : ",  mylist.remove(20)) # removes by value, does not return the value
print("list after remove append returned nothing : ", mylist) # use this after remove append to see the real chnages
print("popped : ", mylist.pop(2)) # removes only the  last element by default, remove by index, returns value after

# tuple -> immutable, ordered -> used for fixed data, 
# mylist[1] = 23 produces a syntax error

#dict -> mutable, ->stores key value pairs
mydict = {"name": "umar",
        "age": 12,
        "class": 13}

print(mydict["age"]) # call the key instead of index to access its value.
mydict["name"] = "ali" 
print(mydict)
print(mydict.keys()) # returns all keys
print(mydict.values()) # returns the values of the keys
print(mydict.items()) # shows both the key->pair mappings

#set -> unique, mutable, unordered
myset = {100, 200, 300, 400}
myset1 = {400, 500, 600, 700}

for i in mylist:
    print(i) # there are no index u must loop thru like linked list

print("none = doesnt return values", myset.remove(200)) # error if value not found
print(myset.add(150)) # 
print(myset.discard(250)) # no error even if value not found
print(myset)

print("union of 2 sets : ", myset | myset1) # all unique values
print("intersections of 2 sets : ", myset & myset1) # only common values in both
print("difference of 2 sets : ", myset - myset1) # uncommon values in both

# slicing -> works on strings, tuple, list
thatlist = [12, 22, 32, 42, 52]
print(thatlist[::-1]) # reverse string
print(thatlist[:3:]) # everything till 3rd index
print(thatlist[1:3]) # start at 1st index and print till end-1

# nested structures
xyzlist = [1, 1, [2, 2], [3, [4, 4]], 0, 0 ]
print(xyzlist[3]) # [3, [4, 4]]
print(xyzlist[3][0]) # [4, 4]
print(xyzlist[3][1][1]) # 4

xylist = [{ "name" : "umar", "age" : 12}, {"name" : "ali", "age" : 13} ]
print(xylist[1]) # entire second dict
print(xylist[1]["age"]) # only age of second dict

xydict = {
    "name" : "umar",
    "age" : 12,
    "address" : { # nested data similar to objects in c++
        "citycode" : 123,
        "city" : "delhi",
        "town" : "town-2"
    }
}
print(xydict["address"]) # entire address block
print(xydict["address"]["city"]) # only one thing inside that data
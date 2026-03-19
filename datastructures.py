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
for i in mylist:
    print(i) # there are no index u must loop thru like linked list

print("none = doesnt return values", myset.remove(200)) # error if value not found
print(myset.add(150)) # 
print(myset.discard(250)) # no error even if value not found
print(myset)
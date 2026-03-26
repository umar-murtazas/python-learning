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

#-------------------------------------------------------# practice
# nlist = []
# for i in range(100):
#     nlist.append(i)
# print(nlist)
nlist = list(range(100))
del nlist[0]
print(nlist)

number = [10, 20, 30, 40, 50]
print(number[:3:])
print(number[:-3:-1])
print(number[::2])

tnumber = (1, 2, 3, 4, 5)
print(tnumber[::-1])

student = {
    "name": "Ali",
    "grades": [80, 90, 85],
    "subjects": ["Math", "Physics", "CS"]
}
print(student["grades"][1])
print(student["subjects"][2])

userlist = [
    {"name" : "umar", "status" : "active"},
    {"name" : "ali", "status" : "not-active"},
    {"name" : "jannat", "status" : "active"}
]
for user in userlist:
    if user["status"] == "active":
        print(user["name"])

newlist = [1, 2, 3, 4, 5, 6,7 ]
llist = [i for i in newlist if i%2 != 0] # list comprehension
print(llist)

network = {
    "routers": [
        {"ip": "192.168.1.1", "port" : 22, "status": "up"},
        {"ip": "192.168.1.2", "port" : 80,  "status": "down"},
    ],
    "switches": [
        {"ip": "192.168.2.1", "port" : 443, "status": "up"},
        {"ip": "192.168.2.2", "port" : 23,  "status": "up"},
        {"ip": "192.168.2.2", "port" : 22,  "status": "down"},
    ]
}
for i in network["routers"] + network["switches"]:
    if i["status"] == "up":
        print(i["ip"])

openportsonly = []
uniqueips = set()
for openports in network["routers"] + network["switches"]:
    if openports["status"] == "up":
        openportsonly.append(openports["port"])
        uniqueips.add(openports["ip"])

print(openportsonly)
print(uniqueips)

users = {
    "Ali": {"admin", "user"},
    "Ahmed": {"user"},
    "Sara": {"admin", "developer"}
}
for admins in users:
    if "admin" in users[admins]:
        print(admins)

lllist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x : not x%2, lllist)) # explicit looping x%2==0 -> False x%2 != 2 -> True
odd = [n for n in lllist if n%2 != 0] # using list comprehension
print(even, odd)

filters = filter(lambda x : not x%2, lllist) # returns memmory address of the object (filters)
print(filters)

data = {
    "servers": [
        {"ip": "1.1.1.1", "services": ["http", "ssh"]},
        {"ip": "2.2.2.2", "services": ["ftp"]},
        {"ip": "3.3.3.3", "services": ["ssh", "ftp", "http"]}
    ]
}
for ips in data["servers"]:  # each dict inside servers will become an iteration now on which ips will iterate
    if "ssh" in ips["services"]: # or u could say ips{ip:}, ips{ip}, ips{ip} ips is the name of those dicts but one at a time
        print(ips["ip"])

ip_addresses = [
    "192.168.1.10",
    "10.0.0.5",
    "192.168.1.10",
    "172.16.0.2",
    "10.0.0.5",
    "192.168.1.20",
    "172.16.0.2",
    "192.168.1.15"
]
uniqueset1 = set()
for i in ip_addresses:
    uniqueset1.add(i)
    print(uniqueset1) 
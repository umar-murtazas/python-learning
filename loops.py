fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits: # stores the value at each iteration
    fruit = fruit.upper()
    print(fruit)

print(fruit) # keeps the last value stored in it
print(fruits) # only the temporary var got changed

# for i in range(0,20,2):   # for known number of iterations
#     print(i)
count = 1
while(count): # for unknown number of iterations
    count += 1
    if(count != 100):
        if(count%2 == 0):
            continue # skips that iteration
        print(count)
    else:
        print("hellooo")
        break #exits the loop

l = ["apple", "bananna", "cocomo"]
for index, fruit in enumerate(l): # pairs each item of the list with a number
    print(index, fruit)

total = 0
for i in range(1, 50): # sum of all
    total += i
print(total)

for a in range(1, 20):
    if(a%2 == 0):
        print(a)

colors = ["red", "green", "blue", "yellow"]
for index, color in enumerate(colors):
    print(index, color)

for b in range(10, 0, -1):
    print(b)

for c in range(1, 30):
    if(c%3==0):
        print("frizz")
    elif(c%5==0):
        print("bizz")
    elif(c%3==0 and c%5==0):
        print("frizzbizz")
    else:
        print(c)

numbered_list = []
for index, color in enumerate(colors):
    numbered_list.append(f"{index}, {color}") # use f for multiple arguments since append only takes one
print(numbered_list)

for m in range(1,5): # right angled traingle
    for n in range(1, m + 1):
        n = m
        print("*", end="") # stops print from moving onto the next line
    print() # moves it to the next line

for o in range(5, 0, -1): #inverted traingle
    for n in range(o):
        print("*", end="")
    print()

row = 1
for p in  range(row, 7, -1):
    print(" " * (row - p) + "*" * (2*p-1))
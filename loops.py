fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits: # stores the value at each iteration
    fruit = fruit.upper()
    print(fruit)

print(fruit) # keeps the last value stored in it
print(fruits) # only the temporary var got changed

for i in range(0,20,2):
    print(i)
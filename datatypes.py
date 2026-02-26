# int
a = 12
# float
b = 12.2
# str
c = "thirteen"
# bool
d = True
# list
e = [1, 2, 4, "hello", "nice"]
# tuple
f = (2, 3, 6, 1, 9)
# set
g = {2, 4, 1, 7, 0}
c = "five"
print(a,b,c,d,e,f,g)

z = [1, 2, 3, 5]
x = z    # rebinding x->z x also points to that list now
x.append(1000)  # any changes in x will also change z
print(z)
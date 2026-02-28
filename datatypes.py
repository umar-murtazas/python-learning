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
# typecasting 
num = "2134.4"  #decimal point str cant be directly cnoverted into int
print(int(float(num)))
num1 = 124
print(str(num1))
aa = "3.14159"
print(float(aa)*2)
ab = "10" 
ac = 10
print(str(ac)+ab) # only strings can be concatenated
ad = 0
ae = 23
print(bool(ae) and bool(ad))
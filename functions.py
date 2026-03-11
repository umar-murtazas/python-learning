def name():
    x = 10 # every var created here will have a local scope
    print(x) 
# print(x) # invalid x doesnt exist outside

def greet(name, age):
    print(name, age)
greet("umar", age=12) # first -> positional argument, second -> keyword argument
#greet(name="umar", 12) # !invalid positional must come before keyword arguments

# args take  positional arguments only
def showargs(*args): # args is conventional but can be of any name
    print(args)
    print(type(args))
    print(args[1])
showargs(1, 2, 3)

def showkwargs(**kwargs): #accepts keywords arguments only
    print(kwargs)
    print(type(kwargs))
    print(kwargs["errors"])
showkwargs(name="umar", age=12, errors="no :)")

# together
def combo(a, *b, **c):
    print(a, b, c)
combo(1, 2, 3, 4, 5, 6, 7, name="waseem", age=66)

# we can unpack kwargs into keyword arguments
def unpackkwargs(name, age):
    print(name, age)
data = {"name":"ahmed", "age":15}
unpackkwargs(**data) # dict will be broken down into keyword arguments like name="ahmed", age=15

#nested functions
def outer():
    def inner():
        print("hello")
    print("bye")
outer()

# lambda -> nameless functions that returns one value
square = lambda x: x**2  # lambda [argument]: {expression}
print(square(8))

# commonly used with filter() -> selects sequence based on a condition
#list() -> convert itrators into lists
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: x%2==0, numbers)) #filter([function, [iterator]])
print(result)

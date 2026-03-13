def hello():
    print("hello world")
hello()

def greet(name):
    print("heelo", name)
greet("umar")

def add(a, b):
    return a + b # return doesnt print values
print(add(3, 5))

def square(a):
    return a**2
print(square(4))

def is_even(a):
    if (a%2==0):
        return True
    elif(a%2!=0):
        return False
print(is_even(12))

def largest(a, b, c):
    if(a > b and c):
        return a
    elif(b > a and c):
        return b
    elif(c > b and a):
        return c
print("largest no is : ", largest(12, 43, 1))

def passwd(password):
    if(len(password) < 8):
        return "weak password"
    elif(len(password) >= 8):
        return "strong password"
print(passwd("@attherate"))

def grade(grades):
    return ("A" if grades >= 90
            else "B" if 80 <= grades < 90
            else "C" if 70 <= grades < 80
            else "D" if 60 <= grades < 70
            else "F" if 0 <= grades < 60 
            else "invalid" )

def sum(a):
    sum = 0
    for i in range(a):
        sum += i
    return sum
print("total sum is :", sum(23))

def factorial(a):
    factorials = 1
    for i in range(1, a):
        factorials *= i
    return factorials
print(factorial(5))


def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum
list = [1, 2, 3, 4, 5, 6]
print(sum_list(list)) # call the name of the data strcuture to use it.

def max_number(list):
    large = list[0]
    for i in list:
        if(large < i):
            large,i = i,large
    return large
print("largest no : ", max_number(list))
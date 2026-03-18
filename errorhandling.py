print("will work")

## syntax error ->  # detected before compilation, nothing gets executed
# if True
    # print("hello world")

##runtime errors -> # detected at runtime, error free lines above gets exceuted regardless

# ------------------------------------------------ # syntax errors
# value errors -> #1 invalid value in the arguments 
# int("string") #invalid converstion
mylist = [1, 2, 3, 4]
# len(mylist) # -> mylist.remove(8)

# type errors -> #2 performing operations between invalid converstions, str + int, list + int
# type() # ->int("string" + 12)

# file not found -> #3 opening files that doesnt exist or wrong path
# open("non_existent.txt")

# index errors -> #4 when u try to access a non existent index
# print(mylist[1]) # -> mylist[7]

# key error -> #5 when u try to access a dict key that doesnt exist
mydict = {"name" : "umar", "age" : 12}
# print(mydict["class"]) # -> print(mydict["name"]) 
 
 # --------------------------------------------------- # handling error
'''
try: #code  that might produce an error
    num = int(input("enter a number : "))
    x = 10/num
    print(x)
except ZeroDivisionError as z: # handles specific errors
    print("Eror : ", z)
except (ValueError, KeyboardInterrupt) as v: # catching multiple exceptions as one
    print("error ->  ", v, end="") 
    print(type(v)) # shows the type of error
finally: # runs evreytime, used for log attempts 
    print("heheh")

if num > 10:
    raise ZeroDivisionError(" number too large! ")

#--------------------------------------------# practice
def num1():
    while True:
        try:
            number = int(input("Enter a number for / 100 : "))
            return 100 / number
        except ZeroDivisionError:
            print("dont enter 0")
        except ValueError:
            print("enter a valid number !")
        finally:
            print("log recorded")
print(num1())

def list_index():
    lists = [10, 20, 30, 40, 50]
    while True:
        try:
            index = int(input("enter a the index u want : "))
            lists[index]
            return lists[index]
        except IndexError:
            print("kindly choose a number below this : ", len(lists))
print(list_index())

def check_age(age):
    try:
        if age < 0:
            raise ValueError("age cant be less then 0")
    finally:
        print("hehhe")
check_age(-1)

def login_check():
        try:
            usrname = input("enter ur username : ")
            passwd = input("enter ur passwd : ")
            if (usrname == "" ):
                raise ValueError("invalid usrname")
            elif(len(passwd) < 8):
                raise ValueError("invalid password")
            return usrname, passwd
        finally:
            print("attempt" )
print(login_check())
'''
def accept_port():
    try:
        port = int(input("enter port"))
    except ValueError:
        print("enter digits only")
    if (port < 65535 and port >= 0):  #always write the if else after exception part
        print(f"successfully connected {port}")
    elif (port > 65535 or port < 0):
        raise ValueError("invald port number")
accept_port()
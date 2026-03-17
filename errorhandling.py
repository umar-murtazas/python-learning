print("will work")

## syntax error ->  # detected before compilation, nothing gets executed
# if True
    # print("hello world")

##runtime errors -> # detected at runtime, error free lines above gets exceuted regardless
# ------------------------------------------------ #
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
 
 # --------------------------------------------------- #
try: #code  that might produce an error
    num = int(input("enter a number : "))
    x = 10/num
    print(x)
except ZeroDivisionError as z: # handles specific errors
    print("Eror : ", z)
except (ValueError, KeyboardInterrupt) as v: # catching multiple exceptions as one
    print("error ->  ", v, end="") 
    print(type(v)) # shows the type of error
finally:
    print("heheh")

if num > 10:
    raise ZeroDivisionError(" number too large! ")
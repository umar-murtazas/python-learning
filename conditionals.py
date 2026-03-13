x = 10
if x >= 10: # basic conditional
    print("hello world")
elif (): # empty things evaluates to False
    print("run?")

# ternary operators
result = 1 if x < 10 else 0 # result stored in the variable result
print(result)

print("yes") if x == 10 else print("no") # print directly so no need of a variable

n = int(input()) # always return an int
# if n%2 == 0:  # check even odd
#     print("even")
# else:
#     print("odd")

# if n > 0:
#     print("positve")
# elif n < 0:
#     print("negative")
# else:
#     print("equal")
## one liner for this
print("positive" if n > 0 else ("negative" if n < 0 else "0"))

# n2 = input()
# if len(n2) < 5:  # len returns length
#     print("short")
# elif len(n2) > 5:
#     print("long")
# else:
#     print("medium")

## one liner only support expressions, break wll throw error
grades = 89
print("A" if grades >= 90
            else "B" if 80 <= grades < 90
            else "C" if 70 <= grades < 80
            else "D" if 60 <= grades < 70
            else "F" if 0 <= grades < 60 
            else "invalid" )       # chaining in conditionals
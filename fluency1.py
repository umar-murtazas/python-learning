# name = input("ur name : ")
# age = input("ur age : ")
# print(f"hello {name}\nu are {age} years old") # use f or they will be printed as it is.

# # 2---------------------------------------------------------------------------------------
# i = []
# i.append(int(input("1 : ")))
# i.append(int(input("2 : ")))
# i.append(int(input("3 : ")))
# try :
#     print(max(list))
# except :
#     i.sort() # sorts in ascending order
#     for j in i:
#         if i[2] > j:
#             j = i
#     print(f"max number is {j}")

# # 3--------------------------------------------------------------------------------------
# sumone = int(input("enter a num : "))
# i = 1
# sum = 0
# while i <= sumone: # in while loops run as long as condition is true.
#     sum += i
#     i += 1
# print(sum)

# # 4----------------------------------------------------------------------------------------
# take = input("enter your line : ")
# vowel = ["a", "e", "i", "o", "u" ]
# vc = 0
# for chr in take:
#     if chr in vowel:
#         vc += 1
# print(vc)

# # 5----------------------------------------------------------------------------------------
# reverse = vowel[::-1]
# print(reverse)
# for i in range(len(vowel)-1, -1, -1): 
#     print(i, vowel[i])

# 6-----------------------------------------------------------------------------------------
student = {
    "name" : "ali",
    "age" : 32,
    "class" : 2
}
print(student.values())

# 7-------------------------------------------------------------------------------------------
def squr(var):
    # global var # cant use global becuase a global var cannot be both a parameter name and a var
    return var**2
par = squr(int(input("multiply your number : ")))
print(par)

# 8-------------------------------------------------------------------------------------------
password = input("enter a pasword : ")
t = "a"
while password != t:
    t = input("retype the password : ")
print("congrats :)")

# 9---------------------------------------------------------------------------------------------
import random
r = random.randint(1,100)
enter = int(input("guess the number : "))
while r != enter:
    if r > enter:
        print("too low")
        enter = int(input("guess the number again : "))    
    elif r < enter:
        print("too high")
        enter = int(input("guess the number again : "))
print("correct")
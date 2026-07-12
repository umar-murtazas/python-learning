# name = input("ur name : ")
# age = input("ur age : ")
# print(f"hello {name}\nu are {age} years old") # use f or they will be printed as it is.

# 2---------------------------------------------------------------------------------------
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

# 3--------------------------------------------------------------------------------------
sumone = int(input("enter a num : "))
i = 1
sum = 0
while i <= sumone:   
    sum += i
    i += 1
print(sum)
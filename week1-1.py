




file = input("file name : ")

with open(file, "r") as f:
    # f.write("hello This is Me\nwe have bEen working oN this project for years\nthe deaDline is deadlined :)")
    content = f.read()
    # print(content)

count = {"uppercase" : 0, "lowercase" : 0, "digit" : 0, "special" : 0}
def count_things(content):
    for words in content:
        for chars in words:
            uc = chars.isupper()
            if(uc == True):
                count["uppercase"] += 1
            lc = chars.islower()
            if(lc == True):
                count["lowercase"] += 1
            d = chars.isdigit()
            if(d == True):
                count["digit"] += 1
            sp  = chars.isalnum()
            if(sp != True and not(chars.isspace())): 
                count["special"] += 1
                print(chars)
    print(count)

def password_length(content):
    return len(content)

# if u want to move in the nested layer under the top condition to not write the entire line again and again use the lower limit
def password_check(content):
    if(not(password_length(content) <= 7 and (count["lowercase"] <= 0 and count["uppercase"] <= 0 ))): 
        if(not(count["digit"] <= 0)):
            if(count["special"] > 0):
                print("password is very strong !!!")
        else:
            print("password is medicore")
    else:
        print("password is very weak")

def print_report(c):
    count_things(c)
    print("totol length is : ", password_length(c))
    password_check(c)
print_report(content)
# -----------------------methods used----------------------------------- #
## isupper() islower() isdigit() isalnum() isspace()
# ----------------------problems----------------------------------------#
## 1) "file" created a file named file instead of var
## 2) count_things() -> functions should return values instead of modify global variables directly
## 3) password_check() -> conditional logic should be readable not complex
## 4) password_check() -> should only count things not print anything.
## 5) second loop should be used only when there are multiple strings in one file.

print("================ password secuirty auditor ================")
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

# --------------------------------------retake------------------------------------------------
# --------------------------------------things used-------------------------------------------
## zip()
# --------------------------------------improvements------------------------------------------
## fucntions dont depend on global var now
## reduced the logical complexity
## each function performs one reposniblity now and returns data instead of modifying directly
# --------------------------------------issues-----------------------------------------------
## wrong logic on last elif
## length_check() inside uses global var instead of local one becuase there is none

user_file = input("enter the name of the file : ")
password = ""
with open(user_file, "r") as file:
    password = file.read()
    print(password)

counts = ["uppercase", "lowercase", "digits", "special"]
def count_things(password):
    upper = lower = digit = special = 0
    for string in password:
        for character in string: # in case of multiple strings
            if character.isupper():
                upper += 1
            elif character.islower():
                lower += 1
            elif character.isdigit():
                digit += 1
            elif not (character.isalnum() and character.isspace()):
                special += 1
            else:
                print("error")
    print(string)
    return upper, lower, digit, special

def pass_length(password):
    return len(password)

def strength_check(counting):
    if(pass_length(password) < 7):
        print("length is too short")
        return
    if(counting[1] <= 0 and counting[0] <= 0):
        print("password is weak")
        return
    if(counting[2] <= 0 and counting[3] <= 0):
        print("password is mediocre :)")
        return
    print("password is strong !!")

def report(p):
    counting = count_things(p)
    total_count = dict(zip(counts, counting))
    print(total_count)
    print("password length is : ", pass_length(p))
    strength_check(counting)
report(password)
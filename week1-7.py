import csv
from datetime import datetime
# -----------------------------------methods used------------------------------------------ #
## 
# -----------------------------------problems---------------------------------------------- #
## 1) used append() so existing data doesnt get overwritten.
## 2) filepointer of normal files can be resetted by seek but module based filepointers (csv, json) should be created again if they get exhausted.
## 3) set() to remove duplicates
## 4) set uses {} but writing this alone will create an empty dict, so use set() for empty set
## 5) max() is function not a method a.max()
## 6) list comprehensiopn will always produce a list so if we only want one value then use [0]
## 7) after opening a file for writing use the var where data is stored not the file pointer
## 8) values must be of the same type, use f{} which automatically converts them into str
## 9) use newline to keep data separated and clean

print(" ========== security log analyzer ==========")

user_file = input("enter the file name : ")
# with open(user_file, "w", newline="") as file:
#     write_obj = csv.writer(file)
#     write_obj.writerow(["name", "afia"])
try:
    with open(user_file, "r", newline="") as file:
        read_file = csv.DictReader(file)
        dictionary = []

        for dicts in read_file:
            dictionary.append(dicts)  # 1
        print(dictionary)

    # for d in read_file:   # 2
    #     print(d["username"])

except FileNotFoundError:
    print("file doesnt exist. please enter a valid name")

def login_info(login_dictionary):
    count_login_attempt, count_success_login, count_failed_login = 0,0,0

    for login_dict in login_dictionary:
        if (login_dict["status"] == "success".upper() or login_dict["status"] == "failed".upper() ):
            count_login_attempt += 1
            if(login_dict["status"] == "SUCCESS"):
                count_success_login += 1
            elif (login_dict["status"] == "FAILED"):
                count_failed_login += 1
        else:
            print("invalid data!!")
            return
    failed_login_percentage =  (count_failed_login / count_login_attempt) * 100
    
    return count_login_attempt, count_failed_login, count_success_login, failed_login_percentage

def user_info(user_dictionary):
    users, ips, failed_login_users, failed_login_ips, most_failed_login_user, most_failed_login_ips = set(), set(), {}, {}, "", ""  # 4
    
    for user_dict in user_dictionary:
        users.add(user_dict["username"])
        ips.add(user_dict["ip"])

    failed_login_users = dict.fromkeys(users, 0)
    failed_login_ips = dict.fromkeys(ips, 0)

    for user_dict in user_dictionary:
        if user_dict["status"] == "FAILED" :
            failed_login_users[user_dict["username"]] += 1
        if user_dict["status"] == "FAILED" :
            failed_login_ips[user_dict["ip"]] += 1

    most_failed_login_user = [key for key,value in failed_login_users.items() if value == max(failed_login_users.values())] # here a stores keys and b stores values
    most_failed_login_ips = [key for key,value in failed_login_ips.items() if value == max(failed_login_ips.values())]
    # most_failed_login_user = failed_login_users["max(failed_login_users.values())"]     # 5
    # most_failed_login_ip = failed_login_users["max(failed_login_ips.values())"]

    for key, value in failed_login_users.items():
        if value >= 3:
            print(key, "your attempt limit has reached!! more attempts could lead to account ban")

    return users, ips, most_failed_login_ips[0], most_failed_login_user[0] #, suspicious_user, suspicious_ip

def create_file_name():
    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = "security_report_" + date + ".txt"
    return file_name

def report(report_dictionary):
    user_data = {
        "total logins" : 0,
        "failed logins" : 0,
        "successful logins": 0,
        "failed logins percentage" : 0,
        "users" : None,
        "ips" : None,
        "username with most failed logins" : None,
        "ip with most failed logins" : None,
    }

    data_list = []
    data_list.extend(login_info(report_dictionary))
    data_list.extend(user_info(report_dictionary))

    final_data = dict(zip(user_data, data_list))
    print(final_data)
    
    file = create_file_name()
    with open(file, "w", newline="") as w:
        for key, value in final_data.items(): # 7
            w.write(f"{key} : {value}\n") #9
            # w.write(key + " : " + value)  # 8
        
report(dictionary)        
import csv
# -------------------------------methods used---------------------------------- #
##
##
##
# -------------------------------problems------------------------------------- #
##
##
## 3) get exacly 5 charcters from the last
## 4) decide biggest on something.

print("================= Failed Login Heatmap =============")

file_name =  input("input the file : ")

try :
    with open(file_name, "r", newline="") as writer:
        # write_data = csv.writer(writer)
        # write_data.writerow(["timestamp", "ip", "username", "status"])
        # write_data.writerow(["2026-08-14 08:12","admin","192.168.1.10","FAILED"])
        # write_data.writerow(["2026-08-14 08:15","john","10.0.0.5","SUCCESS"])
        # write_data.writerow(["2026-08-14 09:01","admin","192.168.1.10","FAILED"])
        # write_data.writerow(["2026-08-14 09:03","admin","192.168.1.10","FAILED"])
        # write_data.writerow(["2026-08-14 13:22","alice","172.16.0.8","SUCCESS"])
        # write_data.writerow(["2026-08-14 23:41","root","185.22.31.4","FAILED"])

        read_data = writer.read()

        lined_data = read_data.split("\r\n")
        

except FileNotFoundError:
    print("the file you serached doesnt exist !!")
    exit

def login_data():
    count_lines,success_attempts,failed_attempts = 0,0,0
    for data in lined_data:
        sep_data = data.split(",")
        if "ip" in sep_data:
            continue
        if sep_data is None:     #1
            continue
        if "success".upper() in sep_data:
            success_attempts += 1
        if "failed".upper() in sep_data:    
            failed_attempts += 1
        
        print(data)
        count_lines += 1

    failure_percetange =  (failed_attempts / count_lines) * 100
    
    return count_lines,success_attempts, failure_percetange

def user_data():
    unique_users, unique_ips = set(), set()
    for useless_user_data in lined_data:
        usefull_data = useless_user_data.split(",")
        print(usefull_data)
        unique_users.add(usefull_data[1])
        unique_ips.add(usefull_data[2])

    return unique_users,unique_ips

def analyze_time():
    times,time,failed_time = "",[],0
    for times_data in lined_data:
        time_data = times_data.split(",")
        if "ip" in time_data:
            continue
        print(time_data)
        times = time_data[0]
        time.append(times[-5:-3])        #3

    failed_time = max(set(time), key=time.count)     #4

    return failed_time

def analyze_users_ips():
    analyze_users,analyze_ips,status,i = [], [],[],0

    for analyze_data in lined_data:
        analyzed_data = analyze_data.split(",")
        if "ip" in analyzed_data:
            continue

        analyze_users.append(analyzed_data[1])
        analyze_ips.append(analyzed_data[2])   
        status.append(analyzed_data[3])

        print(analyzed_data)
    users = dict.fromkeys(analyze_users,[])
    ips = dict.fromkeys(analyze_ips, [])

    for (key,_), (ipkey,_) in zip(users.items(), ips.items()):
        users[key] = [analyze_ips[i], status[i]]    #5 use the key directly instead of writing "key"
        ips[ipkey] = [analyze_users[i], status[i]]    #6 add []
        i += 1

    print(users, ips)

def report():
    # print(login_data())
    # print(user_data())
    # analyze_time()
    analyze_users_ips()


report()
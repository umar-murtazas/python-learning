import csv
# -------------------------------methods used---------------------------------- #
##
##
##
# -------------------------------problems------------------------------------- #
##
##
##
##

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
        print(lined_data)
        # print(read_data)

except FileNotFoundError:
    print("the file you serached doesnt exist !!")
    exit

def login_data():
    count_lines = 0
    for data in lined_data:
        sep_data = data.split(",")
        if "ip" == lined_data:
            continue
        print(sep_data)
        count_lines += 1
    print(count_lines)

def report():
    login_data()

report()
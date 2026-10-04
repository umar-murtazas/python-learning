import requests as req
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin, urlparse
from datetime import datetime 

link = input("enter the link : ")

try :
    start = time.perf_counter()     # measures the time of whatevers between it.
    response = req.get(link, timeout=5)
    end = time.perf_counter()       # one perf gives the current time so we end -start to find the actual time it took.
    response_time = end - start
    response.raise_for_status

    soup = BeautifulSoup(response.text, "html.parser")

    domain = link.split("/")        # 2 would always contain the domain name.

    
except req.exceptions.RequestException as e:     # built in to handle req based errors, 
    print("request failed : ", e)
except ModuleNotFoundError as f:
    print("module not found : ", f)

# reponse info
def reponse_info(response):
    print("status code : ", response.status_code)
    print("final url : ", response.url)
    print("response time : ", response_time)
    print("response size : ", response.headers["Date"])
    print("content-Type : ", response.headers["Content-Type"])

# check headers
def reponse_header(response):
    security_headers = ["Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy",
    "Permissions-Policy"]

    for header,value in response.headers.items():       # use items to unpack both values else only one would get unpacked but 2 varaibles to take it.
        # print(header, " : ", value)
        if header in security_headers:
            print(header, " : MISSING")
        else:
            print(header, " : PRESENT")

# extract links
def reponse_link_extraction(soup, domain):        
    internal_link_counter = 0
    external_link_counter = 0
    for links in soup.find_all("a"):
        if links.text.startswith("/") or "/" not in links.text:       # if non zero value then its true else false.
            full_link = urljoin(link, links.text)       # use href that conatins the entire link thats more useful.
            internal_link_counter += 1
            print(full_link)
        elif links.href:
            ex_domain = links.href.split("/")
            if ex_domain == domain[2]:
                external_link_counter += 1
        else:
            print("error :)")
            print(ex_domain[2])

    print(internal_link_counter)
    print(external_link_counter)

def response_imp_path(soup):            
    imp_paths = [ "admin", "login", "api", "upload", "dashboard", "user," "register", "Zyte" ] # zyte for testing behaviour only

    for paths in soup.find_all("a"):
        if paths.text in imp_paths:
            path = urljoin(link, paths.text)
            print("imp path found : ", path)

def file_name_timestamp():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    filename = f"web_recon_{timestamp}.txt"

    print(filename)
    # open (timestamp)
def summary():
    reponse_info(response)
    reponse_header(response)
    reponse_link_extraction(soup, domain)
    response_imp_path(soup)
    file_name_timestamp()
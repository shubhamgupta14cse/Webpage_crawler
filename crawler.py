import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import urljoin

def request(url):
    try:

        r=requests.get(url)
        return r.content

    except requests.exceptions.ConnectionError or requests.exceptions.InvalidURL or requests.exceptions.MissingSchema:
        pass


target_url="https://www.rottentomatoes.com"
target_links=[]

def subdomain():
    with open("./subdomains-100.txt","r") as wordlist:
        for line in wordlist:
            word=line.strip()
            test_url=word +"."+ target_url
            response=request(test_url)
            if response:
                print("[+] Discovered Subdomain ---> "+test_url)

def directory():
    with open("./common.txt","r") as wordlist:
        for line in wordlist:
            word= line.strip()
            test_url = target_url + "/" + word
            response = request(test_url)
            if response:
                print("[+] Discovered Url -->"+ test_url)



def extract_links(url):
    r=request(url)
    link_list=[]
    try:
        soup=BeautifulSoup(r ,  "html.parser")
        for a in soup.find_all('a', href=True):
            link_list.append(a['href'])
        return link_list
    except:
        return link_list    







def crawl(url):
    href_links=extract_links(url)
    for link in href_links:
        link=urljoin(url ,link)


        if "#" in link:
            link=link.split("#")[0]
        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            try:
                crawl(link)
            except:
                pass






crawl(target_url)

for link in target_links:
    print(link)
    
    
subdomain()
directory()


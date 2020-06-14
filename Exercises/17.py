import requests
from bs4 import BeautifulSoup
url='http://www.nytimes.com'
r=requests.get(url)
soup=BeautifulSoup(r.text)
headline_data=soup.find_all("h2")
for item in headline_data:
    print(item.find("span").text) if item.find("span") else print(item.text)

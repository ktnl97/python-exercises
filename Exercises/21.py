import requests
from bs4 import BeautifulSoup
def get_headline_text():
    url='http://www.nytimes.com'
    r=requests.get(url)
    soup=BeautifulSoup(r.text)
    headline_data=soup.find_all("h2")
    headline_string = ""
    for item in headline_data:
        headline_string += (item.find("span").text) if item.find("span") else item.text
        headline_string += "\n"
    return headline_string

open_file = open('file_to_save.txt', 'w')
open_file.write(get_headline_text())
open_file.close()
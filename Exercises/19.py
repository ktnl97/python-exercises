import requests

from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

article = soup.find_all('p')

[print(i.text) for i in soup.find_all('p')]

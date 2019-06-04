import requests
from bs4 import BeautifulSoup as bs

page =  requests.get("https://www.wsj.com/articles/global-bond-yields-hit-multiyear-lows-11559068245")
soup = bs(page.content, 'html.parser')

list = soup.findAll('p')

for s in list:
    print(s.getText())
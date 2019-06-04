from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

url = "https://www.wsj.com/articles/global-bond-yields-hit-multiyear-lows-11559068245"
html = (urlopen(url)).read()
soup = bs(html.decode("utf-8"), "html.parser")
print(soup.body)
with open("output.html", "w") as file:
    file.write(str(soup.body.prettify().encode("utf-8")))
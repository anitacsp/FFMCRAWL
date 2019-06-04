#WSJ Example

import requests
from bs4 import BeautifulSoup as bs

#Enter site map index
page =  requests.get("https://www.wsj.com/sitemaps/web/wsj/en/sitemap_wsj_en_index.xml")
soup = bs(page.content, 'html.parser')

#Finds index page for each quarter
list = soup.findAll('loc')

#Iterate through each quarter's link
for s in list:
    print(s.getText())
    quarter = s.getText()
    qPage = requests.get(quarter)
    s = bs(qPage.content, 'html.parser')
    #Find links for each news article from each quarter
    qlist = s.findAll('loc')
    #Print links
    for l in qlist:
           print(l.getText())
    break

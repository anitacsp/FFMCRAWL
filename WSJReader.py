#@gaybirdy
#Test for specifically WSJ sitemap
#
import requests
from bs4 import BeautifulSoup as bs

class WSJReader:
    #words that should be replaced
    replacementWords = ["u s", "u k"]

    #creates a wsjreader object that stores the given url
    def __init__(self,WSJURL):
        self.url = WSJURL

    #accesses & retrieve content of specified page
    def getPage(self):
        page =  requests.get(self.url)
        content = bs(page.content, 'html.parser')

        return content

    #access & retrieve a list of sitemaps for each quarter
    def quarterIndex(self):
        content = self.getPage()
        urlList = content.findAll('loc')

        return urlList

    #retrieves a list of article links
    def articleIndex(self, url):
        link = url.getText()
        print("quarter: " + link)
        page =  requests.get(link)
        content = bs(page.content, 'html.parser')

        urlList = content.findAll('loc')

        return urlList
    
    #extracts title from url & cleans any words that needs replacement
    def getTitle(self,url):
        
        removeDomain = url.rsplit('/',1)
        almostTitle = removeDomain[1]

        removeBackNum = almostTitle.rsplit('-',1)
        dashedTitles = removeBackNum[0]

        cleanTitle = dashedTitles.replace("-", " ")

        for r in self.replacementWords:
            if r in cleanTitle:
                
                store = r
                country = store.replace(" ", "").upper()

                cleanTitle = cleanTitle.replace(r,country)


        return cleanTitle

    









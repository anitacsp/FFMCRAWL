import requests
from bs4 import BeautifulSoup as bs

class WSJReader:

    def __init__(self,WSJURL):
        self.url = WSJURL

    def getPage(self):
        page =  requests.get(self.url)
        content = bs(page.content, 'html.parser')

        return content

    def quarterIndex(self):
        content = self.getPage()
        urlList = content.findAll('loc')

        return urlList

    def articleIndex(self, url):
        link = url.getText()
        print("quarter: " + link)
        page =  requests.get(link)
        content = bs(page.content, 'html.parser')

        urlList = content.findAll('loc')

        return urlList

    def getTitle(self,url):
        
        removeDomain = url.rsplit('/',1)
        almostTitle = removeDomain[1]

        removeBackNum = almostTitle.rsplit('-',1)
        dashedTitles = removeBackNum[0]

        cleanTitle = dashedTitles.replace("-", " ")
        return cleanTitle









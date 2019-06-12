#@gaybirdy
#Generic sitemap reader
#
import titleRetriever

import numpy as np
import requests
from bs4 import BeautifulSoup as bs


class siteReader:

    #creates a reader object that stores the given url
    def __init__(self, URL):
        self.url = URL

    def changeSite(self,URL):
        self.url = URL


    #accesses & retrieve content of specified page
    def getPage(self):
        page =  requests.get(self.url)
        content = bs(page.content, 'html.parser')

        return content

    def getDates(self):
        content = self.getPage()
        date = content.findAll('news:publication_date')
        #print(date)
        return date

    #access & retrieve a list of sitemaps for each quarter
    def index(self):
        content = self.getPage()
        urlList = content.findAll('loc')
       
        return urlList

    #retrieves a list of article links
    def articleIndex(self, url):
        link = url.getText()
        #print("quarter: " + link)
        page =  requests.get(link)
        content = bs(page.content, 'html.parser')

        urlList = content.findAll('loc')

        return urlList

    def iterateIndex(self, indexUrl, tr, sc, endYear):
        array = []
        print(type(array))
        for map in indexUrl:
            if endYear in map.getText():
                print(map)
                break
            articleList = self.articleIndex(map)

            for article in articleList:
                url = article.getText()
                title = tr.getTitle(url)
                score = sc.analyze(title)

                row = sc.prettyRow(title, score, url)
                array.append(row)
        
        return array 

    def iterateArticle(self, articleURL, pubDate, tr, sc, endYear):
        array = []
        for article, date in zip(articleURL, pubDate):
            if endYear in date.getText():
                print(date)
                break

            url = article.getText()
            title = tr.getTitle(url)
            #print(title)
            score = sc.analyze(title)

            row = sc.prettyRow(title, score, url)
            #print(row)
            array.append(row)

        return array 

    pass





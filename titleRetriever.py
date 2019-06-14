#@gaybirdy
#Generic title retriever
#
import requests
from bs4 import BeautifulSoup as bs
import csv

class titleRetriever:
     replacementWords = ["u s", "u k"]

     #create TR object
     def __init__(self,web):
        self.website = web
     
     #if TR is used for more than one site
     def changeSite(self, web):
         self.website = web
    
     #depending on which site, title retrieval varies
     def getTitle(self, url):
         
         if self.website == 'WSJ':
             #print('WSJ!')
             title = self.wsjTitle(url)
             print(title)
         if self.website == 'et':
             #print('et')
             title = self.etTitle(url)
         if self.website == 'indianexpress':
            title = self.ieTitle(url)
         if self.website == 'scmp':
            title = self.scmp(url)
         if self.website == 'bbg':
            title = self.scmp(url)

         return title

     #stores content to specified filepath
     def toCSV(self, outputFilename, content):

        csvHeader = ["Title" ,  "compound" ,"sent", "Link to article"]

        with open(outputFilename, 'w', newline = "") as file:
            writer = csv.writer(file)
            writer.writerow(csvHeader)
            #print(type(content))
            for row in content: 
                writer.writerow(row)
                
            
        print("Output to "+outputFilename+" successful!")
    
     def etTitle(self, url):

         split = url.rsplit('/')
         dashedTitle = split[len(split)-3]

         cleanTitle = dashedTitle.replace("-", " ")
         cleanTitle = self.clean(cleanTitle)
         return cleanTitle

     def wsjTitle(self,url):
        removeDomain = url.rsplit('/',1)
        almostTitle = removeDomain[1]

        removeBackNum = almostTitle.rsplit('-',1)
        dashedTitles = removeBackNum[0]

        cleanTitle = dashedTitles.replace("-", " ")
        cleanTitle = self.clean(cleanTitle)

        return cleanTitle

     def ieTitle(self,url):
        url = url[0:len(url)-1]

        return self.wsjTitle(url)
     
     def scmp(self, url):
         removeDomain = url.rsplit('/',1)
         almostTitle = removeDomain[1]

         cleanTitle = almostTitle.replace("-", " ")
         cleanTitle = self.clean(cleanTitle)

         return cleanTitle
     
     def clean(self, title):
        for r in self.replacementWords:
            if r in title:
                
                store = r
                country = store.replace(" ", "").upper()

                title = title.replace(r,country)

        return title

     pass





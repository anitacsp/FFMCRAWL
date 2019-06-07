#@gaybirdy 
import WSJReader as WSJR
import sentimentAnalysis as SA
import csv

#Header for csv
csvHeader = ["Title" ,"Neg ", "Neu" , "Pos" , "Composite" , "Link to article"]

#sitemap from robots.txt
xmlLink = "https://www.wsj.com/sitemaps/web/wsj/en/sitemap_wsj_en_index.xml"

wsj = WSJR.WSJReader(xmlLink)
print("wsjreader object created")
sentimentCheck = SA.sentimentAnalysis()
print("sentimentanalysis object created")


#retrieve sitemap for each quarter 
qLinkList = wsj.quarterIndex()
print("Get quarters")



#opens designated file location 
with open('wsjSentiment.csv', 'w' , newline="") as file:
    writer = csv.writer(file)
    writer.writerow(csvHeader)

    #iterates through each quarter's sitemap
    for qlink in qLinkList:
        #finds the link to each article
        quarter = wsj.articleIndex(qlink)

        for q in quarter:
            url = q.getText()
            #print("articles: "+ url)
            #extract title from url
            title = wsj.getTitle(url)
            #print(title)
            score = sentimentCheck.analyze(title)
            
            row = sentimentCheck.prettyRow(title, score, url)
            #writes to designated location
            writer.writerow(row)

file.close()    

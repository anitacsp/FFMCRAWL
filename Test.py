import WSJReader as WSJR

xmlLink = "https://www.wsj.com/sitemaps/web/wsj/en/sitemap_wsj_en_index.xml"

wsj = WSJR.WSJReader(xmlLink)
print("wsj object created")

qLinkList = wsj.quarterIndex()
print("Get quarters")

for qlink in qLinkList:
    quarter = wsj.articleIndex(qlink)

    for q in quarter:
        url = q.getText()
        print("articles: "+ url)
        print(wsj.getTitle(url))
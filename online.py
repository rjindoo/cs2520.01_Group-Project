import urllib.request
stockLabel = input("Enter Stock Label: ").upper()
page = urllib.request.urlopen("http://www.finance.yahoo.com/quote/"+stockLabel)
pageText = page.read()
decodedPageText = pageText.decode("utf-8")
#location = decodedPageText.find("<span class=")
#print(decodedPageText[location:location + 97])
query = "<span class="
find = lambda sentence, qry: sentence[sentence.find(qry):sentence.find(qry)+97] if qry in sentence else -1

htmlLineWithPrice = find(decodedPageText, query)
#parse htmlLineWithPrice to only have price
stockPrice = ""
with open(stockLabel + ".csv",'a') as outFile:
	print(htmlLineWithPrice)
	#outFile.write(stockPrice))

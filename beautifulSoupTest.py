from bs4 import BeautifulSoup
import urllib.request
import csv

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
def getStockLabelHeader():
	try:
		with open('./csvFiles/averageStockFile' + '.csv', 'r') as readFile:
			reader = csv.reader(readFile)
			stockLabelHeader = next(reader)
	except:
		stockLabelHeader = []
	return stockLabelHeader

#print(getStockLabelHeader())

def writeStockFile(label, price):
	stockLablFile = csv.writer(open(stockLabel + ".csv", "a"))
	stockLablFile.writerow(["test","test1","test2"])
	#with open("./csvFiles" + stockLabel + ".csv",'a') as outFile:
	print(stockLabel,htmlLineWithPrice)
		#outFile.write(stockPrice))

writeStockFile(stockLabel, htmlLineWithPrice)
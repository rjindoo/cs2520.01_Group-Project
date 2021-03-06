from bs4 import BeautifulSoup
import urllib.request
import csv

stockLabel = input("Enter Stock Label: ").upper()
page = urllib.request.urlopen("http://www.finance.yahoo.com/quote/"+stockLabel)
pageText = page.read()
decodedPageText = pageText.decode("utf-8")
#location = decodedPageText.find("<span class=")
#print(decodedPageText[location:location + 97])
yahooQuery = "<span class="
find = lambda sentence, qry: sentence[sentence.find(qry):sentence.find(qry)+97] if qry in sentence else -1

htmlLineWithPrice = find(decodedPageText, yahooQuery)
#parse htmlLineWithPrice to only have price
stockPrice = htmlLineWithPrice.split(" ")[-1].split(">")[1].split("<")[0]

def getStockLabelHeader():
	try:
		with open('./csvFiles/averageStockFile' + '.csv', 'r') as readFile:
			reader = csv.reader(readFile)
			stockLabelHeader = next(reader)
	except:
		stockLabelHeader = []
	return stockLabelHeader


def writeStockFile(label, price):
	try:
		stockLablFile = csv.writer(open('./csvFiles/' + stockLabel + ".csv", "a"))
		stockLablFile.writerow([price])
	except:
		return -1
	return 0
def main():
	#print(getStockLabelHeader())
	
	if writeStockFile(stockLabel, stockPrice) == 0:
		print("File write success.")
	else:
		print("File not written.")
	

if __name__ == '__main__':
	main()
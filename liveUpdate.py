import urllib.request
import os

stockLabel = input("Enter Stock Label: ").upper()
os.system('cls' if os.name == 'nt' else 'clear')
while True:
	page = urllib.request.urlopen("http://www.finance.yahoo.com/quote/"+stockLabel)
	pageText = page.read()
	decodedPageText = pageText.decode("utf-8")
	query = "<span class="
	find = lambda sentence, qry: sentence[sentence.find(qry):sentence.find(qry)+97] if qry in sentence else -1

	htmlLineWithPrice = find(decodedPageText, query)
	#parse htmlLineWithPrice to only have price
	stockPrice = htmlLineWithPrice.split(" ")[-1].split(">")[1].split("<")[0]
	print('\r%s: %s' % (stockLabel,stockPrice), end = '\r')
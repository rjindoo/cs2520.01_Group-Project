import urllib.request
page = urllib.request.urlopen("http://www.finance.yahoo.com/quote/DIS")
pageText = page.read()
decodedPageText = pageText.decode("utf-8")
#location = decodedPageText.find("<span class=")
#print(decodedPageText[location:location + 97])
query = "<span class="
find = lambda sentence, qry: sentence[sentence.find(qry):sentence.find(qry)+97] if qry in sentence else -1
s = find(decodedPageText, query)
with open("cvx.csv",'a') as cvxOut:
	print(s)
	#cvxOut.write(find(decodedPageText, query))

#print(find(decodedPageText, "<span class="))
'''
<span class="Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)" data-reactid="14">86.09</span>
find(‘div’,{‘class’: ‘My(6px) Pos(r) smartphone_Mt(6px)’})
'''
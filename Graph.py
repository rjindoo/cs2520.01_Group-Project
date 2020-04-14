import matplotlib.pyplot as plt
import csv

stockLabel = input("Enter Stock Label: ")
stockPrices = []
with open('./csvFiles/' + stockLabel + '.csv', newline='') as file:
	reader = csv.reader(file)
	for val in reader:
		stockPrices.append(''.join(val))

stockPrices = list(map(float, stockPrices))
for val in stockPrices:
	plt.plot(stockPrices)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

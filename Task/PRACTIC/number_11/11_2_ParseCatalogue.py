import re
import ssl
import urllib.request
ssl._create_default_https_context= ssl._create_unverified_context


url= "https://quke.ru/shop/smartfony/apple?page-size=72"
response = urllib.request.urlopen(url).read().decode()

namePattern = r"(?:\d\"\,\s+\"name\"\:\s\")([^\"]*)"
name = re.findall(namePattern, response)

pricePattern = r"(?:\"price\"\:\s)([^\n]*)"
price = re.findall(pricePattern, response)

namePriceList = []

for i in range(len(name) - 1):
    namePriceList.append([name[i], int(price[i])])

totalPhones = 0
totalSumPrices = 0
minPrice = 9999999
maxPrice = -1

for i in namePriceList:
    if i[1] > maxPrice:
        maxPrice = i[1]
    if i[1] < minPrice:
        minPrice = i[1]
    totalPhones += 1
    totalSumPrices += i[1]

for i in namePriceList:
    if i[1] == maxPrice:
        print(f"Самый дорогой смартфон: {i}")
    if i[1] == minPrice:
        print(f"Самый дешевый смартфон: {i}")
averagePrice = totalSumPrices / totalPhones
print(f"Средняя цена всех смартфонов: {round(averagePrice, 2)}")


catalog = open("11_2_catalog.txt", "w")

catalog.write("Название смартфона | ")
catalog.write("Цена в рублях \n")
for i in namePriceList:
    catalog.write(' | '.join(str(s) for s in i) + '\n')

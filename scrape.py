import csv
import requests
from bs4 import BeautifulSoup

url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('tbody', attrs={'class': 'stripe'})


list_of_rows = []
list_of_rows2 = []
for row in table.findAll('tr'):
	list_of_cells = []
	for cell in row.findAll('td'):
		text = cell.text.replace('Details', '')
		list_of_cells.append(text)
	list_of_rows.append(list_of_cells)

for row in list_of_rows:
	row.pop(0)
	list_of_rows2.append(row)

with open("./inmates.csv", "wb") as outfile:
	writer = csv.writer(outfile)
	writer.writerows(list_of_rows)
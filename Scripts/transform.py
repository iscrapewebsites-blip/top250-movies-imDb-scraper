import csv
import json
from openpyxl import Workbook
from openpyxl.styles.fonts import Font

data = []
with open('output.json', 'r', encoding='utf-8') as f:
     data = json.loads(f.read())

header = list(data[0].keys())
with open('output.csv', 'w', encoding='utf-8') as f:
     writer = csv.DictWriter(f, fieldnames=header)
     writer.writeheader()
     writer.writerows(data)


wb = Workbook()
ws = wb.active

ws.append(header)

for dict in data:
     ws.append(list(dict.values()))
 
for cell in ws['1']:
     cell.font = Font(bold=True)

wb.save('output.xlsx')


     
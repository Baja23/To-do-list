import csv

#Program do utworzenia nowej listy zadań

headerList = ['temat', 'termin', 'opis', 'data rozpoczęcia', 'status']

with open('Lista zadań.csv', 'w') as file:
    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
    dw.writeheader()


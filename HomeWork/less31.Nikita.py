import csv

with open('library.csv', 'a', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Название', 'Автор', 'Год']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, skipinitialspace=True)
    writer.writeheader()
    writer.writerow({'Название': 'Богатый папа', 'Автор': 'Роберт', 'Год': '2007'})

with open('library.csv',encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, skipinitialspace=True)
    for row in reader:
        print(row['Название'], row['Автор'], row['Год'])
import csv
import re



with open('data-398-2018-08-30.csv', encoding='utf8', newline='') as csv_file:
    busreader = csv.reader(csv_file)
    lst = []
    for row in busreader:
        col1, col2, col3 = row[1], row[4], row[6]
        col1 = re.sub('\(\d+\)', '', col1)
        col_gen = col1 + col2 + col3
        lst.append({
            'Name': col1,
            'Street': col2,
            'District': col2,
        })
        print(col3)

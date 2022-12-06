import csv

dataArr=list()
data = dict()

dataParse = dict()
fieldName = []
with open('newMasterFIle.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        fieldName= row
        break

with open('parse.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            line_count +=1
        else:
            dataParse[row['ID']] = row

with open('newMasterFIle.csv', mode='r', encoding='ISO-8859-1') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            line_count +=1
        else:
            # if row['Batch Month'] !='' and row['Command'] == 'MERGE':
            dataArr.append(row)
            data[row['ID']]=row




print(data)
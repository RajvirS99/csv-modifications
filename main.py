import csv

data = dict()

fieldName = []
dataArr = list()

with open('dr.vranjes.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        fieldName = row
        break

with open('dr.vranjes.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            line_count +=1
        else:
            if row['Batch Month'] !='' and row['Command'] == 'MERGE':
                dataArr.append(row)


with open('parse.csv', mode='w') as csv_file:

    writer = csv.DictWriter(csv_file, fieldnames=fieldName)
    writer.writeheader()
    for i in range(0, len(dataArr)):
        writer.writerow(dataArr[i])

print(dataArr[0])
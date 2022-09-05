import csv

# Author Nathan Fenwick
# Python file is responsible for interacting with the stored CSVs

def openCSV(csvName):
    with open(csvName, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader)
        for row in reader:
            print(', '.join(row))
        csvfile.close()


def appendCSV(csvName, items):
    cleanCSV(csvName)
    with open(csvName, 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for x in items:
            writer.writerow(x)
        csvfile.close()


def cleanCSV(csvName):
    with open(csvName, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["amount", "category", "date", "name", "newBalance", "previousBalance", "reference", "timeDiff", "dayOfWeek"])
    csvfile.close()

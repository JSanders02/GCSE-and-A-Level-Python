def importCSV(CSVName):
    with open(str(CSVName), 'rt') as text_file:
        reader = csv.reader(text_file)
        importList = list(reader)
        return importList
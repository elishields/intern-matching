import sys
import numpy
import pandas

# Filepath to Excel object as param
def loadExcel(excel_file):
    # Read first sheet from Excel into pandas DataFrame (2D table)
    dataset = pandas.read_excel(excel_file)
    return dataset

def cleanData(dataset):
    for index, row in dataset.iterrows():
        short_name = ""
        for char in row[0]:
            if len(short_name) < 12:
                short_name += char
        row[0] = short_name
        print (row[0])
    return dataset

# Verify that each intern name is unique
def checkData(dataset):
    names = []
    for index, row in dataset.iterrows():
        names.append(row[0])
    names = numpy.array(names)
    name, occurrences = numpy.unique(names, return_counts=True)
    counted_names = dict(zip(name, occurrences))
    if not all(count == 1 for count in counted_names.values()):
        sys.exit("Multiple occurrences of a name.")
    return (len(names))

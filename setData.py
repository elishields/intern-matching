import re
import sys
import numpy
import pandas

# Read Excel sheet into pandas DataFrame (2-dimensional table)
def loadExcel(excel_file):
    dataset = pandas.read_excel(excel_file)
    return dataset

def cleanData(dataset):
    dataset = cleanCharacters(dataset)
    # dataset = shortenNames(dataset)
    return dataset

# Remove non-whitespace and non-alphabet characters from dataset
def cleanCharacters(dataset):
    for index, row in dataset.iterrows():
        for col in range(5):
            # cleaned_data = re.sub("[\s^a-zA-Z]+", "", row[col])
            cleaned_data = re.sub("([^\s\w]|_)+", "", row[col])
            row[col] = cleaned_data
    return dataset

# Shorten names to 10 characters
def shortenNames(dataset):
    for index, row in dataset.iterrows():
        short_name = ""
        for char in row[0]:
            if len(short_name) < 10:
                short_name += char
        row[0] = short_name
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

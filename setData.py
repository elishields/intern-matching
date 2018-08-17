import re
import sys
import json
import numpy
import pandas


# Read Excel sheet into pandas DataFrame (2-dimensional table)
def load_excel(excel_file):
    dataset = pandas.read_excel(excel_file)
    return dataset


def clean_data(dataset):
    dataset = strip_nonalpha_chars(dataset)
    dataset = rename_keywords(dataset)
    dataset = strip_duplicates(dataset)
    return dataset


# Remove non-whitespace and non-alphabet characters from dataset
def strip_nonalpha_chars(dataset):
    for index, row in dataset.iterrows():
        for col in range(5):
            print(row[col])
            cleaned_data = re.sub("([^\s\w]|_)+", "", row[col])
            # cleaned_data = cleaned_data.lower()
            # row[col] = cleaned_data
    return dataset


def rename_keywords(dataset):
    keywords_map = json.load(open("keywords_map.json"))
    for keyword_key, keyword_value in keywords_map.items():
        for index, row in dataset.iterrows():
            for col in range(5):
                row[col] = row[col].replace(keyword_key, keyword_value)
    return dataset


def strip_duplicates(dataset):
    # create a set
    return dataset


# Shorten names to 10 characters
def shorten_names(dataset):
    for index, row in dataset.iterrows():
        short_name = ""
        for char in row[0]:
            if len(short_name) < 10:
                short_name += char
        row[0] = short_name
    return dataset


# Verify that each intern name is unique
def check_data(dataset):
    names = []
    for index, row in dataset.iterrows():
        names.append(row[0])
    names = numpy.array(names)
    name, occurrences = numpy.unique(names, return_counts=True)
    counted_names = dict(zip(name, occurrences))
    if not all(count == 1 for count in counted_names.values()):
        sys.exit("Multiple occurrences of a name.")
    return (len(names))

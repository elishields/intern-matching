import sys
import numpy
import pandas
from openpyxl import *
from intern import Intern
from collections import OrderedDict

# Filepath to Excel object as param
def loadExcel(excel_file):
    # Read first sheet from Excel into pandas DataFrame (2D table)
    dataset = pandas.read_excel(excel_file)
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

# Create intern objects with attributes read
def createInterns(dataset, interns_count):
    interns = []
    row = 1
    for intern, in dataset.iter_rows(max_col=1):
        if intern.value != None:
            newIntern = Intern(row, intern.value)
            interns.append(newIntern)
            sendAttributes(dataset, newIntern, row)
            row += 1
        if intern.value == None:
            return interns
    return interns

def createInterns(dataset):
    interns = []
    for index, row in dataset.iterrows():

        newIntern = Intern(index, row[0])
        interns.append(newIntern)
        sendAttributes(dataset, newIntern, index)


# Read attributes from spreadsheet and pass to intern instance variables
def sendAttributes(dataset, intern, row):
    att_list = []
    for cell, in dataset.iter_cols(min_row=row, max_row=row, min_col=2, max_col=5):
        att_list.append(cell.value)
    attributes = (att_list[0], att_list[1], att_list[2], att_list[3])
    intern.setAttributes(attributes)

# Max rounds is each intern pairing with every other intern
def getRounds(interns):
    return len(interns) - 1

def getIntern(interns, intern_name):
    intern_name = str(intern_name)
    for intern in interns:
        if intern.name == intern_name:
            return intern

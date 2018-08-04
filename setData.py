import sys
import pandas
from openpyxl import *
from collections import OrderedDict

from intern import Intern

# Filepath to Excel object as param
def loadExcel(excel_file):
    # Read Excel table into pandas DataFrame (2D table)
    # Reads first sheet by default
    dataset = pandas.read_excel(excel_file)
    return dataset

# Load Excel spreadsheet into iterable columns and rows
# def loadExcel(raw_data):
#     workbook = load_workbook(raw_data, data_only=True)
#     spreadsheet = workbook["InternData"]
#     return spreadsheet

# Verify that each intern name is unique
def checkData(dataset):
    names = []
    for intern, in dataset.iter_rows(max_col=1, max_row = 9):
        names.append(intern.value)
    for name in names:
        matching_names = 0
        for name_compare in names:
            if name == name_compare:
                matching_names += 1
            if matching_names > 1:
                sys.exit("multiple instances of " + name)

# Create intern objects with attributes read
def createInterns(dataset):
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

from openpyxl import *
from intern import Intern
from collections import OrderedDict
from pairingFunctions import *

dataset = []

def loadExcel(raw_data):
    global dataset
    workbook = load_workbook(raw_data, data_only=True)
    spreadsheet = workbook["InternData"]
    dataset = spreadsheet
    return spreadsheet

def createInterns():
    interns = []
    count = 1
    for intern, in dataset.iter_rows(max_col=1, max_row = 9):
        newIntern = Intern(count, intern.value)
        interns.append(newIntern)
        count += 1
    return interns

def getAttributes(internRow):
    att_list = []
    for cell, in dataset.iter_cols(min_row=internRow, max_row=internRow, min_col=2, max_col=5):
        att_list.append(cell.value)
    attributes_tuple = (att_list[0], att_list[1], att_list[2], att_list[3])
    return attributes_tuple

def checkData(table):
    names = []
    for intern, in dataset.iter_rows(max_col=1, max_row = 9):
        names += intern.value
    for name in names:
        for name_compare in names:
            matching_names = 0
            if name == name_compare:
                matching_names += 1
            if matching_names > 1:
                sys.exit(matching_names, "instances of", name)

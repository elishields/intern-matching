import pandas
from intern import Intern

# def createInterns(dataset):
#     interns = []
#     row = 1
#     for intern, in dataset.iter_rows(max_col=1):
#         if intern.value != None:
#             newIntern = Intern(row, intern.value)
#             interns.append(newIntern)
#             sendAttributes(dataset, newIntern, row)
#             row += 1
#         if intern.value == None:
#             return interns
#     return interns

# Create intern objects with attributes read
def createInterns(dataset):
    # Array of Intern objects
    interns = []
    for index, row in dataset.iterrows():
        if len(row) > 0:
            # Location in spreadsheet, name
            newIntern = Intern(index, row[0])
            interns.append(newIntern)
            sendAttributes(dataset, newIntern, index)
        else:
            return interns
    return interns

# def sendAttributes(dataset, intern, row):
#     att_list = []
#     for cell, in dataset.itercols():
#         att_list.append(cell.value)
#     attributes = (att_list[0], att_list[1], att_list[2], att_list[3])
#     intern.setAttributes(attributes)

# Set intern instance variables with attributes from dataset
def sendAttributes(dataset, intern, row):
    att_list = []
    for index, attributes in dataset.iterrows():
        if index == row:
            att_list = (attributes[0], attributes[1], attributes[2], attributes[3])
    intern.setAttributes(attributes)

def getIntern(interns, intern_name):
    intern_name = str(intern_name)
    for intern in interns:
        if intern.name == intern_name:
            return intern

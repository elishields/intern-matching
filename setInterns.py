import pandas
from intern import Intern

# Create intern objects with attributes read
# def createInterns(dataset):
#     # Array of Intern objects
#     interns = []
#     for index, row in dataset.iterrows():
#         if len(row) > 0:
#             # Location in spreadsheet, name
#             newIntern = Intern(index, row[0])
#             interns.append(newIntern)
#             print ("sending", newIntern.name)
#             sendAttributes(dataset, newIntern, index)
#         else:
#             return interns
#     return interns

# Create intern objects
def createInterns(dataset):
    interns = []
    for row in dataset.itertuples():
        newIntern = Intern(row.Index, row.NAME)
        interns.append(newIntern)
        sendAttributes(dataset, newIntern, row.Index)
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
            att_list = (attributes[1], attributes[2], attributes[3], attributes[4])
    intern.setAttributes(attributes)
    print (attributes)

def getIntern(interns, intern_name):
    intern_name = str(intern_name)
    for intern in interns:
        if intern.name == intern_name:
            return intern

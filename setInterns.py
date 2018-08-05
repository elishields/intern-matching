import pandas
from intern import Intern

# Create intern objects
def createInterns(dataset):
    interns = []
    for row in dataset.itertuples():
        newIntern = Intern(row.Index, row.NAME)
        interns.append(newIntern)
        sendAttributes(dataset, newIntern, row.Index)
    return interns

# Set intern instance variables
def sendAttributes(dataset, intern, location):
    for row in dataset.itertuples():
        if row.Index == location:
            att_list = (row.TEAM, row.POSITION, row.PRODUCT, row.SKILLS)
            intern.setAttributes(att_list)
            return

def getIntern(interns, intern_name):
    for intern in interns:
        if intern.name == intern_name:
            return intern

def getChaosIntern(interns):
    for intern in interns:
        if intern.name == "chaos_intern":
            return intern

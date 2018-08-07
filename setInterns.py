import pandas
from intern import Intern

# Create intern objects
def createInterns(dataset):
    interns = []
    for row in dataset.itertuples():
        newIntern = Intern(row.Index, row.NAME)
        interns.append(newIntern)
        sendAttributes(dataset, newIntern, row.Index)
    # if len(interns) % 2 != 0:
    interns.append(releaseChaosIntern(interns))
    return interns

# Set intern instance variables
def sendAttributes(dataset, intern, location):
    for row in dataset.itertuples():
        if row.Index == location:
            intern.team = row.TEAM
            intern.position = row.POSITION
            intern.product = row.PRODUCT
            intern.skills = row.SKILLS

def releaseChaosIntern(interns):
    row = len(interns)
    name = "chaos"
    chaos = Intern(row, name)
    for attribute in ["team", "position", "product", "skills"]:
        chaos.attribute = "generic"
    return chaos

def printInterns(interns):
    for intern in interns:
        print (intern.row, intern.name)

def getChaosIntern(interns):
    for intern in interns:
        if intern.name == "chaos":
            return intern

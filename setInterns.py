import pandas
from intern import Intern

# Create intern objects
def createInterns(dataset):
    interns = []
    for row in dataset.itertuples():
        newIntern = Intern(row.Index, row.NAME)
        print (row.Index, row.NAME)
        interns.append(newIntern)
        sendAttributes(dataset, newIntern, row.Index)
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
    name = "chaos_intern"
    chaos_intern = Intern(row, name)
    interns.append(chaos_intern)
    for attribute in ["team", "position", "product", "skills"]:
        chaos_intern.attribute = "generic"
    print ("")
    print("SMITHERS, RELEASE THE CHAOS_INTERN")
    print("YES MR. BURNS, RELEASING THE CHAOS INTERN")
    print("*CHUCKLES*")
    print("*RUBS HANDS*")
    print("*CHUCKLES AGAIN*")
    print("VERY GOOD SMITHERS")
    print("NO ONE IS SAFE MR. BURNS")
    print("NO ONE IS SAFE")
    print("X__X")
    return interns

def getChaosIntern(interns):
    for intern in interns:
        if intern.name == "chaos_intern":
            return intern

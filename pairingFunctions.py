from intern import Intern
from collections import OrderedDict
from helperFunctions import *

def setPairs(interns):
    for intern in interns:
        setEndorsers(intern, interns)
        rankEndorsers(intern)
        pruneEndorsers(intern)
        # pairEndorsers(interns)

def setEndorsers(intern, interns):
    for other_intern in interns:
        if intern.name != other_intern.name:
            score = scorePair(intern, other_intern)
            intern.endorsers.update({other_intern.name: score})

# compare intern attributes
def scorePair(intern, other_intern):
    compatibility_score = 0
    for attribute in ["team", "position", "product", "skills"]:
        for word in getattr(intern, attribute).split():
            if word in getattr(other_intern, attribute).split():
                compatibility_score += 1
    return compatibility_score

# order endorsers by quantity of matches
def rankEndorsers(intern):
    intern.endorsers = OrderedDict(sorted(intern.endorsers.items(), key=lambda kv: kv[1], reverse=True))

# remove endorsers with no matches
def pruneEndorsers(intern):
    intern.endorsers = {key: value for key, value in intern.endorsers.items() if value is not 0}

def getPairs(interns):
    for intern in interns:
        print (intern.name.upper())
        for key, value in intern.endorsers.items():
            print (key + "\t" + str(value))
        print ("\n")

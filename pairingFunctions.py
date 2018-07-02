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
    attributes = ["team", "position", "product", "skills"]
    matching_words = []
    for attribute in attributes:
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

# implement stable marriage algo
# https://en.wikipedia.org/wiki/Stable_marriage_problem#Algorithm
def pairEndorsers(interns):
    rounds = len(interns) / 2
    for round in range(rounds):
        marry(interns)

# def marry(interns):
#     pairs = {}
#     for intern in interns:
#         pairs.update({intern: 0})
#     while 0 in pairs.values():
#       print (deez nyets)

def getPairs(interns):
    for intern in interns:
        print (intern.name.upper())
        for key, value in intern.endorsers.items():
            print (key + "\t" + str(value))
        print ("\n")

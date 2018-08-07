from intern import Intern
from collections import OrderedDict

# Record each intern's compatibility with every other intern
def setEndorsers(session, interns):
    for intern in interns:
        for other_intern in interns:
            if other_intern is not intern:
                score = scoreEndorser(intern, other_intern)
                intern.endorsers.update({other_intern.name: score})
        rankEndorsers(intern)

# Count similar attributes between a pair of interns
def scoreEndorser(intern, other_intern):
    compatibility_score = 0
    for attribute in ["team", "position", "product", "skills"]:
        for word in getattr(intern, attribute).split():
            if word in getattr(other_intern, attribute).split():
                compatibility_score += 1
    compatibility_score += 1
    if intern.name == "chaos" or other_intern.name == "chaos":
        compatibility_score = 0
    return compatibility_score

# Order endorsers dictionary by quantity of matches
def rankEndorsers(intern):
    intern.endorsers = OrderedDict(sorted(intern.endorsers.items(), key=lambda kv: kv[1], reverse=True))

# Remove endorsers with no compatibililty from dictionary
def pruneEndorsers(intern):
    intern.endorsers = {key: value for key, value in intern.endorsers.items() if value is not 0}

# Print out endorsers for each intern in name:rank format
def getEndorsers(interns):
    for intern in interns:
        print (intern.name.upper())
        for key, value in intern.endorsers.items():
            print (key + "\t" + str(value))
        print ("\n")

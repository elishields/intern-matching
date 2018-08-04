from intern import Intern
from setData import *

# Each round everyone gets married and the marriages are stable
def setPairs(rounds, interns):
    # For each round during the entire session
    for round in range(rounds):
        # Every intern begins the round free to match
        initializePairs(round, interns)
        # While there is still an intern free to match
        while findUnpaired(round, interns) is not None:
            # Pair the next free intern in interns
            intern = findUnpaired(round, interns)
            # Highest scoring preference
            # Has not yet been proposed to by this intern in this round
            # Has not matched with this intern in a previous round
            preferred_intern = getPreferred(round, intern, interns)
            # If the preferred intern is free to match
            print (intern, "HAS PREFERENCE", preferred_intern)
            print (intern.pairs[round][2])
            if checkFree(round, interns, preferred_intern):
                # Pair the compatible interns
                # Add them to each other's proposed list in case they become unmatched
                newPair(round, intern, preferred_intern, interns)
            # If the preferred intern is not free to match
            else:
                # If the preferred intern prefers this intern to preferred intern's current match
                if isProposalAccepted(round, intern, preferred_intern, interns):
                    previous_match = getIntern(interns, preferred_intern).pairs[round][0]
                    # Free both sides of their outranked match
                    free(round, previous_match, interns)
                    free(round, preferred_intern, interns)
                    newPair(round, intern, preferred_intern, interns)
                # If the preferred intern prefers their current match to this intern
                else:
                    intern.pairs[round][2].append(preferred_intern)

def initializePairs(round, interns):
    for intern in interns:
        # {round: [counterparty, rank, [proposed]]}
        intern.pairs.update( { round: [ None, None, [] ] } )

def findUnpaired(round, interns):
    for intern in interns:
        if intern.pairs[round][0] is None:
            return intern

def getPreferred(round, intern, interns):
    # Starts from highest score
    for endorser_key, endorser_value in intern.endorsers.items():
        if not hasProposed(round, intern, endorser_key) and not hasMatched(round, intern, endorser_key):
            return getIntern(interns, endorser_key)

def hasProposed(round, intern, endorser):
    print (intern.pairs[round][2])
    return endorser in intern.pairs[round][2]

def hasMatched(round, intern, endorser):
    for previousRound in range(round):
        if intern.pairs[round][0] == endorser:
            return True
    return False

def checkFree(round, interns, preferred_intern):
    return getIntern(interns, preferred_intern).pairs[round][0] is None

def newPair(round, intern, preferred_intern, interns):
    compatibility_score = 0
    for endorser_name, endorser_score in intern.endorsers.items():
        if endorser_name == preferred_intern:
            compatibility_score = endorser_score
    # intern.pairs[round][0] = preferred_intern
    # intern.pairs[round][1] = compatibility_score
    # if preferred_intern not in intern.pairs[round][2]:
    #     intern.pairs[round][2].append(preferred_intern)
    getIntern(interns, intern).pairs[round][0] = preferred_intern
    getIntern(interns, intern).pairs[round][1] = compatibility_score
    if preferred_intern not in getIntern(interns, intern).pairs[round][2]:
        getIntern(interns, intern).pairs[round][2].append(preferred_intern)
    getIntern(interns, preferred_intern).pairs[round][0] = intern
    getIntern(interns, preferred_intern).pairs[round][1] = compatibility_score
    getIntern(interns, preferred_intern).pairs[round][2].append(intern)

def isProposalAccepted(round, intern, preferred_intern, interns):
    compatibility_score = getIntern(interns, preferred_intern).endorsers[intern.name]
    # PROBABLY SHOULD BE USING INTERN.NAME FOR THE KEY
    existing_match_score = getIntern(interns, preferred_intern).pairs[round][1]
    return compatibility_score > existing_match_score

def free(round, intern, interns):
    getIntern(interns, intern).pairs[round][0] = None
    getIntern(interns, intern).pairs[round][1] = None

def getPairs(interns):
    for intern in interns:
        print (intern.name.upper())
        for key, value in intern.pairs.items():
            print (key, str(value[0]))
        print ("\n")

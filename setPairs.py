from intern import Intern

# Each round everyone gets married and the marriages are stable
def setPairs(round, interns):
    initializePairs(round, interns)
    while checkUnpairedExists(round, interns):
        for intern in interns:
            preferred_intern = getPreferred(round, intern)
            if checkFree(round, preferred_intern):
                newPair(round, intern, preferred_intern)
            else:
                if isProposalAccepted(round, intern, preferred_intern):
                    old_marriage = preferred_intern.pairs[round][0]
                    free(round, old_marriage)
                    free(round, preferred_intern)
                    newPair(round, intern, preferred_intern)
                else:
                    intern.endorsers[round][2].update(preferred_intern)

def initializePairs(round, interns):
    for intern in interns:
        intern.pairs[round] = [None, None, None]

def checkUnpairedExists(round, interns):
    for intern in interns:
        if intern.pairs[round] is None:
            return True
    return False

def getPreferred(round, intern):
    for endorser in intern.endorsers:
        if checkUnproposed(round, intern, endorser):
            return endorser

def checkUnproposed(round, intern, endorser):
    return endorser in intern.pairs[round][2]

def checkFree(round, preference):
    return preference.pairs[round] is None

def newPair(round, intern, preferred_intern):
    preferred_intern_score = 0
    for endorser_name, endorser_score in intern.endorsers:
        if endorser_name == preferred_intern.name:
            preferred_intern_score = endorser_score
    intern.pairs[round][0] = preference
    intern.pairs[round][1] = preference_score

def isProposalAccepted(round, proposing_intern, preferred_intern):
    proposing_intern_rank = intern.endorsers[intern]
    preferred_intern_current_marriage_rank = preferred_intern.pairs[round][1]
    return proposing_intern_rank > preferred_intern_current_marriage_rank

def free(round, not_intern):
    not_intern.pairs[round] = None

def getPairs(interns):
    for intern in interns:
        print (intern.name.upper())
        for key, value in intern.pairs.items():
            print (key, str(value[0]))
        print ("\n")

from intern import Intern
from setInterns import getIntern

def initializePairs(round, interns):
    for intern in interns:
        intern.pairs.update({ round: [None, None, []] })

def unpairedExists(round, interns):
    for intern in interns:
        if intern.pairs[round][0] is None:
            return intern

def findIdealMatch(round, intern, interns):
    for endorser_name, endorser_score in intern.endorsers.items():
        if hasNotProposed(round, intern, endorser_name) and hasNotMatched(round, intern, endorser_name):
            for look_for_intern in interns:
                if look_for_intern.name == endorser_name:
                    return look_for_intern

def hasNotProposed(round, intern, endorser):
    return endorser not in intern.pairs[round][2]

def hasNotMatched(round, intern, endorser):
    for previousRound in range(round):
        if intern.pairs[round][0] == endorser:
            return False
    return True

def checkFree(round, interns, ideal_match):
    return ideal_match.pairs[round][0] is None

def rankPair(intern, match):
    for endorser_name, endorser_score in intern.endorsers.items():
        if endorser_name == match:
            return endorser_score

def pair(round, intern, match, rank):
    intern.pairs[round][0] = match
    intern.pairs[round][1] = rank
    if match not in intern.pairs[round][2]:
        intern.pairs[round][2].append(match)
    match.pairs[round][0] = intern
    match.pairs[round][1] = rank
    if intern not in match.pairs[round][2]:
        match.pairs[round][2].append(intern)

def proposeNewPair(round, intern, match, proposed_rank):
    current_rank = match.pairs[round][1]
    if match not in intern.pairs[round][2]:
        intern.pairs[round][2].append(match)
    return proposed_rank > current_rank

def free(round, intern, interns):
    current_match = intern.pairs[round][0]
    intern.pairs[round][0] = None
    intern.pairs[round][1] = None
    for intern in interns:
        if intern.name == current_match:
            intern.pairs[round][0] = None
            intern.pairs[round][1] = None

def setPairs(rounds, interns):
    for round in range(rounds):
        initializePairs(round, interns)
        while unpairedExists(round, interns) is not None:
            intern_to_pair = unpairedExists(round, interns)
            ideal_match = findIdealMatch(round, intern_to_pair, interns)
            if checkFree(round, interns, ideal_match):
                rank = rankPair(intern_to_pair, ideal_match)
                pair(round, intern_to_pair, ideal_match, rank)
            else:
                if proposeNewPair(round, intern_to_pair, ideal_match, rank):
                    free(round, ideal_match, interns)
                    pair(round, intern_to_pair, ideal_match, rank)

def getPairs(interns):
    for intern in interns:
        print (intern.name.upper())
        for key, value in intern.pairs.items():
            print (key, str(value[0]))
        print ("\n")

from intern import Intern
from setInterns import getChaosIntern

def setPairs(session, interns):
    for round in range(session.num_rounds):
        beginRoundUnmatched(round, interns)
        while unpairedExists(round, interns) is not None:
            intern_to_pair = unpairedExists(round, interns)
            ideal_match = findIdealMatch(round, intern_to_pair, interns)
            if ideal_match == None:
                ideal_match = getChaosIntern(interns)
            rank = rankPair(intern_to_pair, ideal_match)
            if checkFree(round, ideal_match):
                pair(round, intern_to_pair, ideal_match, rank)
            else:
                if proposalAccepted(round, intern_to_pair, ideal_match, rank):
                    free(round, ideal_match, interns)
                    print ("PAIRING " + intern_to_pair.name + " AND " + ideal_match.name)
                    pair(round, intern_to_pair, ideal_match, rank)

def beginRoundUnmatched(round, interns):
    for intern in interns:
        intern.pairs.update({ round: [None, 0, []] })

def unpairedExists(round, interns):
    for intern in interns:
        if intern.pairs[round][0] is None:
            return intern

def findIdealMatch(round, intern_to_pair, interns):
    for endorser_name, endorser_score in intern_to_pair.endorsers.items():
        if hasNotProposed(round, intern_to_pair, endorser_name) and hasNotMatched(round, intern_to_pair, endorser_name):
            for look_for_intern in interns:
                if look_for_intern.name == endorser_name:
                    return look_for_intern
    return None

def hasNotProposed(round, intern_to_pair, endorser):
    return endorser not in intern_to_pair.pairs[round][2]

def hasNotMatched(round, intern_to_pair, endorser):
    if intern_to_pair.pairs[round][0] is not None:
        if "chaos_intern" in intern_to_pair.pairs[round][0]:
            return False
    for previous_round in range(round):
        if "chaos_intern" in intern_to_pair.pairs[previous_round][0]:
            return True
        if intern_to_pair.pairs[previous_round][0] == endorser:
            return False
    return True

def checkFree(round, ideal_match):
    return ideal_match.pairs[round][0] is None

def rankPair(intern_to_pair, match):
    for endorser_name, endorser_score in intern_to_pair.endorsers.items():
        if endorser_name == match.name:
            return endorser_score

def pair(round, intern, match, rank):
    print ("PAIRING " + intern.name + " AND " + match.name)
    intern.pairs[round][0] = match.name
    intern.pairs[round][1] = rank
    if match.name not in intern.pairs[round][2]:
        intern.pairs[round][2].append(match.name)
    match.pairs[round][0] = intern.name
    match.pairs[round][1] = rank
    if intern.name not in match.pairs[round][2]:
        match.pairs[round][2].append(intern.name)

def proposalAccepted(round, intern, match, proposed_rank):
    if match.name not in intern.pairs[round][2]:
        intern.pairs[round][2].append(match.name)
    current_rank = match.pairs[round][1]
    if current_rank is 0:
        return True
    return proposed_rank > current_rank

def free(round, intern, interns):
    current_match = intern.pairs[round][0]
    intern.pairs[round][0] = None
    intern.pairs[round][1] = 0
    for intern in interns:
        if intern.name == current_match:
            intern.pairs[round][0] = None
            intern.pairs[round][1] = 0

def getPairs(interns):
    for intern in interns:
        print (intern.name.upper())
        print ("-ROUND-\t\t -MATCH-\t\t-RANK-")
        for key, value in intern.pairs.items():
            print (key, "\t\t", value[0], "\t\t", value[1])
        print ("\n")

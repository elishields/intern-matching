from intern import Intern
from utils import printHeader
from setInterns import getChaosIntern

def setPairs(session, interns):
    for round in range(session.num_rounds):
        beginRoundUnmatched(round, interns)
        while (unpairedExists(round, interns) is not None) and (unpairedExists(round, interns).name != "chaos"):
            intern_to_pair = unpairedExists(round, interns)
            ideal_match = findIdealMatch(round, intern_to_pair, interns)
            if ideal_match == None:
                ideal_match = getChaosIntern(interns)
            rank = rankPair(intern_to_pair, ideal_match)
            propose(round, intern_to_pair, ideal_match, rank, interns)

def beginRoundUnmatched(round, interns):
    for intern in interns:
        intern.pairs.update({ round: [None, 0, []] })

def unpairedExists(round, interns):
    for intern in interns:
        if intern.pairs[round][0] is None:
            return intern

def findIdealMatch(round, intern, interns):
    for endorser_name, endorser_score in intern.endorsers.items():
        if (not previousProposal(round, intern, endorser_name)) and (not previousMatch(round, intern, endorser_name)):
            for look_for_intern in interns:
                if look_for_intern.name == endorser_name:
                    return look_for_intern
    return None

def previousProposal(round, intern, endorser):
    return endorser in intern.pairs[round][2]

def previousMatch(round, intern, endorser):
    if intern.name == "chaos" or endorser == "chaos":
        return False
    for previous_round in range(round):
        if endorser in intern.pairs[previous_round][0]:
            return True
    return False

def propose(round, intern, match, rank, interns):
    intern.pairs[round][2].append(match.name)
    if checkFree(round, match):
        pair(round, intern, match, rank)
    else:
        if proposalAccepted(round, intern, match, rank):
            free(round, match, interns)
            pair(round, intern, match, rank)

def checkFree(round, ideal_match):
    return ideal_match.pairs[round][0] is None

def rankPair(intern, match):
    for endorser_name, endorser_score in intern.endorsers.items():
        if endorser_name == match.name:
            return endorser_score

def pair(round, intern, match, rank):
    intern.pairs[round][0] = match.name
    intern.pairs[round][1] = rank
    match.pairs[round][0] = intern.name
    match.pairs[round][1] = rank

def proposalAccepted(round, intern, match, proposed_rank):
    current_rank = match.pairs[round][1]
    return proposed_rank >= current_rank

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
        print("\n" + intern.name.upper())
        for key, value in intern.pairs.items():
            round = str(key) + ": "
            match = value[0]
            score = "(" + str(value[1]) + ")"
            if match == None:
                match = "None"
            print (round + match + score)

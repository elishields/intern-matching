from intern import Intern

# https://en.wikipedia.org/wiki/Stable_marriage_problem#Algorithm
# def stableMatching():
    # while round <= rounds
        # while exists unpaired intern
            # ideal_intern = highest unproposed intern on list
            # if ideal_intern is free
                # pair(intern, ideal_intern)
            # else if pair (!intern, ideal_intern) exists
                # if ideal_intern prefers intern
                    # free(!intern)
                    # pair (intern, ideal_intern)
                # else
                    # (!intern, ideal_intern) stay paired
                    # intern moves on

def setPairs(interns):
    round = len(interns) - 1
    for round in range(rounds):
        if checkUnpairedExists(round, interns) != None:
            ideal_intern = checkUnpairedExists(round, interns)

    def checkFree(round, ideal_intern):
        if ideal_intern.pairs[round] == None:
            return True
        else:
            return False

    def newPair(round, intern, ideal_intern):
        ideal_intern_rank = 0
        for endorser in intern.endorsers:
            if endorser.name == ideal_intern.name:
                ideal_intern_rank = endorser.value()
        intern.pairs[round] = [ideal_intern, ideal_intern_rank]

    def free(round, not_intern):
        intern.pairs[round] = None

    def compareIdeal(intern, not_intern):
        intern_rank = 0
        not_intern_rank = 0
        intern.endorsers[intern].value

    def checkUnpairedExists(round, interns):
        for intern in interns:
            if intern.pairs[round] == None:
                return intern
        return None

def getPairs(interns):
    for intern in interns:
        for pair in intern.pairs:
            print (pair)
        print ("\n")

# function stableMatching {
#     Initialize all m ∈ M and w ∈ W to free
#     while ∃ free man m who still has a woman w to propose to {
#        w = first woman on m’s list to whom m has not yet proposed
#        if w is free
#          (m, w) become engaged
#        else some pair (m', w) already exists
#          if w prefers m to m'
#             m' becomes free
#            (m, w) become engaged
#          else
#            (m', w) remain engaged
#     }
# }

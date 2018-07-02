# implement stable marriage algo
# https://en.wikipedia.org/wiki/Stable_marriage_problem#Algorithm
def stableMatching():
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

    variables:
        current round
        intern
            free
    functions:
        checkFree(ideal_intern)
        pair(intern, ideal_intern)
        free(not_intern, ideal_intern)
        checkIdeal(intern, not_intern)




def pairEndorsers(interns):
    rounds = len(interns) - 1
    for round in range(rounds):
        findPartners(interns)

# def findPartners(interns):
#     pairs = {}
#     for intern in interns:
#         pairs.update({intern: 0})
#     while 0 in pairs.values():
#

function stableMatching {
    Initialize all m ∈ M and w ∈ W to free
    while ∃ free man m who still has a woman w to propose to {
       w = first woman on m’s list to whom m has not yet proposed
       if w is free
         (m, w) become engaged
       else some pair (m', w) already exists
         if w prefers m to m'
            m' becomes free
           (m, w) become engaged
         else
           (m', w) remain engaged
    }
}

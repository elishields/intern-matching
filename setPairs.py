# from intern import Intern
#
# # https://en.wikipedia.org/wiki/Stable_marriage_problem#Algorithm
# # def stableMatching():
#     # while round <= rounds
#         # while exists unpaired intern
#             # ideal_intern = highest unproposed intern on list
#             # if ideal_intern is free
#                 # pair(intern, ideal_intern)
#             # else if pair (!intern, ideal_intern) exists
#                 # if ideal_intern prefers intern
#                     # free(!intern)
#                     # pair (intern, ideal_intern)
#                 # else
#                     # (!intern, ideal_intern) stay paired
#                     # intern moves on
#
# # Each round everyone gets married and the marriages are stable
# def setPairs(interns):
#     rounds = len(interns) - 1
#     for round in range(rounds):
#         if checkUnpairedExists(round, interns):
#             for intern in interns:
#                 ideal_intern = getIdeal(round, intern)
#                 if checkFree(round, ideal_intern):
#                     newPair(round, intern, ideal_intern)
#                 else:
#                     ideal_intern_preference = compareIdeal(round, intern, ideal_intern)
#
#     def checkUnpairedExists(round, interns):
#         for intern in interns:
#             if intern.pairs[round] == None:
#                 return True
#         return None
#
#     def getIdeal(intern):
#         for endorser in intern.endorsers:
#             if checkFree(round, endorser):
#                 return endorser
#
#     def checkFree(round, ideal_intern):
#         if ideal_intern.pairs[round] == None:
#             return True
#         else:
#             return False
#
#     def newPair(round, intern, ideal_intern):
#         ideal_intern_rank = 0
#         for endorser_name, endorser_score in intern.endorsers:
#             if endorser_name == ideal_intern.name:
#                 ideal_intern_rank = endorser_score
#         intern.pairs[round] = [ideal_intern, ideal_intern_rank]
#
#     def compareIdeal(round, intern, ideal_intern):
#         current_pair_rank = ideal_intern.pairs[round]
#         intern.endorsers[intern].value
#
#     def free(round, not_intern):
#         intern.pairs[round] = None
#
# def getPairs(interns):
#     for intern in interns:
#         for pair in intern.pairs:
#             print (pair)
#         print ("\n")
#
# # function stableMatching {
# #     Initialize all m ∈ M and w ∈ W to free
# #     while ∃ free man m who still has a woman w to propose to {
# #        w = first woman on m’s list to whom m has not yet proposed
# #        if w is free
# #          (m, w) become engaged
# #        else some pair (m', w) already exists
# #          if w prefers m to m'
# #             m' becomes free
# #            (m, w) become engaged
# #          else
# #            (m', w) remain engaged
# #     }
# # }

from setInterns import get_chaos_intern


def set_pairs(session, interns):
    for round in range(session.num_rounds):
        begin_round_unmatched(round, interns)
        while (unpaired_exists(round, interns) is not None) and (unpaired_exists(round, interns).name != "chaos"):
            intern_to_pair = unpaired_exists(round, interns)
            ideal_match = find_ideal_match(round, intern_to_pair, interns)
            if ideal_match is None:
                ideal_match = get_chaos_intern(interns)
            rank = rankPair(intern_to_pair, ideal_match)
            propose(round, intern_to_pair, ideal_match, rank, interns)


def begin_round_unmatched(round, interns):
    for intern in interns:
        intern.pairs.update({ round: [None, 0, []] })


def unpaired_exists(round, interns):
    for intern in interns:
        if intern.pairs[round][0] is None:
            return intern


def find_ideal_match(round, intern, interns):
    for endorser_name, endorser_score in intern.endorsers.items():
        if (not previous_proposal(round, intern, endorser_name)) and (not previous_match(round, intern, endorser_name)):
            for look_for_intern in interns:
                if look_for_intern.name == endorser_name:
                    return look_for_intern
    return None


def previous_proposal(round, intern, endorser):
    return endorser in intern.pairs[round][2]


def previous_match(round, intern, endorser):
    if intern.name == "chaos" or endorser == "chaos":
        return False
    for previous_round in range(round):
        if endorser in intern.pairs[previous_round][0]:
            return True
    return False


def propose(round, intern, match, rank, interns):
    intern.pairs[round][2].append(match.name)
    if check_free(round, match):
        pair(round, intern, match, rank)
    else:
        if proposal_accepted(round, intern, match, rank):
            free(round, match, interns)
            pair(round, intern, match, rank)


def check_free(round, ideal_match):
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


def proposal_accepted(round, intern, match, proposed_rank):
    current_rank = match.pairs[round][1]
    return proposed_rank > current_rank


def free(round, intern, interns):
    current_match = intern.pairs[round][0]
    intern.pairs[round][0] = None
    intern.pairs[round][1] = 0
    for intern in interns:
        if intern.name == current_match:
            intern.pairs[round][0] = None
            intern.pairs[round][1] = 0


def get_pairs(interns):
    for intern in interns:
        print("\n" + intern.name.upper())
        for key, value in intern.pairs.items():
            round = str(key + 1) + ": "
            match = value[0]
            score = "(" + str(value[1]) + ")"
            if len(match) < 7:
                match += "\t\t\t"
            elif len(match) > 15:
                match += "\t"
            else:
                match += "\t\t"
            print(" " + round + "\t" + match + " " + score)

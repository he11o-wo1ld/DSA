def stableInternships(interns, teams):
    # Write your code here.
    matchings = {}
    available_interns = [True]*len(interns)

    while any(available_interns):

        for intern, is_available in enumerate(available_interns):
            if is_available:
                break

        team = interns[intern][0]
        del interns[intern][0]

        if team not in matchings:
            matchings[team] = intern
            available_interns[intern] = False
        else:
            current_intern = matchings[team]
            if teams[team].index(intern) < teams[team].index(current_intern):
                matchings[team] = intern
                available_interns[intern] = False
                available_interns[current_intern] = True
    return [[val, key] for key, val in matchings.items()]


interns = [
    [0, 1, 2, 3],
    [0, 1, 3, 2],
    [0, 2, 3, 1],
    [0, 2, 3, 1]
    ]
teams = [
    [1, 3, 2, 0],
    [0, 1, 2, 3],
    [1, 3, 2, 0],
    [3, 0, 2, 1]
    ]
print(stableInternships(interns, teams))
def get_points_from_round_result(round):
    """
    A X rock
    B Y paper
    C Z scissor

    """

    p1 = round[0]
    p2 = round[2]

    if p1 == "A" and p2 == "Z":
        return 0
    if p1 == "C" and p2 == "Y":
        return 0
    if p1 == "B" and p2 == "X":
        return 0

    if p1 == "A" and p2 == "X":
        return 3
    if p1 == "B" and p2 == "Y":
        return 3
    if p1 == "C" and p2 == "Z":
        return 3

    if p1 == "B" and p2 == "Z":
        return 6
    if p1 == "C" and p2 == "X":
        return 6
    if p1 == "A" and p2 == "Y":
        return 6
    

def get_points_from_played_hand(round):
    """
    Returns the partial points for a round based on the second players hand
    """
    hand_points = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    return hand_points[round[2]]

def get_points_from_outcome(round):
    outcome_points = {
        "X": 0,
        "Y": 3,
        "Z": 6,
    }
    return outcome_points[round[2]]

def get_points_from_figured_out_hand(round):
    p1 = round[0]
    p2 = round[2]

    if p1 == "A" and p2 == "Z":
        return 2
    if p1 == "C" and p2 == "Y":
        return 3
    if p1 == "B" and p2 == "X":
        return 1

    if p1 == "A" and p2 == "X":
        return 3
    if p1 == "B" and p2 == "Y":
        return 2
    if p1 == "C" and p2 == "Z":
        return 1

    if p1 == "B" and p2 == "Z":
        return 3
    if p1 == "C" and p2 == "X":
        return 2
    if p1 == "A" and p2 == "Y":
        return 1

with open("/workspaces/advent-of-code/2022/02-input.txt", "r", encoding="utf-8") as rounds:
    total_score = 0
    for round in rounds:
        print(round, end="")
        print(get_points_from_figured_out_hand(round), get_points_from_outcome(round), "\n")
        total_score += get_points_from_figured_out_hand(round) + get_points_from_outcome(round)
    print("The total score is", total_score)

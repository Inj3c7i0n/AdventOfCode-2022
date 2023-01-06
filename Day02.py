#!/usr/bin/python3

# Getting the input DATA
with open('Day02.in') as file:
    rounds = [i.replace(" ", "") for i in file.read().strip().split('\n')]

# View Data
# print(rounds)

# All possible outcomes written out
# ---------------------------------------------
# LEFT VS RIGHT | OUT | RIGHT + OUTCOME = TOTAL
# ---------------------------------------------
# A vs X = DRAW = (1 + 3) = 4
# A vs Y = WIN  = (2 + 6) = 8
# A vs Z = LOSS = (3 + 0) = 3
# B vs X = LOSS = (1 + 0) = 1
# B vs Y = DRAW = (2 + 3) = 5
# B vs Z = WIN  = (3 + 6) = 9
# C vs X = WIN  = (1 + 6) = 7
# C vs Y = LOSS = (2 + 0) = 2
# C vs Z = DRAW = (3 + 3) = 6


# Set all possible outcomes in key:value form.
outcomes = {
    "AX": 4, "AY": 8, "AZ": 3,
    "BX": 1, "BY": 5, "BZ": 9,
    "CX": 7, "CY": 2, "CZ": 6
}

# Create our variable to keep score.
total_score_p1 = 0

# Traverse through our data
# and add the outcome(score) to our
# current score.
for round in rounds:
    total_score_p1 += outcomes[round]

print("Answer to Part 1:", total_score_p1)


# Desired outcomes
# Change 2nd column depending on outcome
# round should have.
realOutcomes = {
    "AX": 3, "AY": 4, "AZ": 8,
    "BX": 1, "BY": 5, "BZ": 9,
    "CX": 2, "CY": 6, "CZ": 7
}

# Create variable for the real outcome
# (according) to the strategy guide rules
total_score_p2 = 0

for round in rounds:
    total_score_p2 += realOutcomes[round]

print("Answer to Part 2:", total_score_p2)
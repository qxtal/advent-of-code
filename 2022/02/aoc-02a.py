#!/usr/bin/env python3
# Advent of Code 2022: Day 2 (part 1)
# Submission by qxtal <quartz@xtal.sh>

f = open('./input.txt', 'r')
game_input = f.readlines()
f.close()

# This can definitely be done in a better way, but it works.
lookup = {
    "X": {          # Player: ROCK
        "A": 1 + 3,     # Opponent: Rock    - TIE
        "B": 1 + 0,     # Opponent: Paper   - LOSS
        "C": 1 + 6      # Opponent: Scissor - WIN
    },
    "Y": {          # Player: PAPER
        "A": 2 + 6,     # Opponent: Rock    - WIN
        "B": 2 + 3,     # Opponent: Paper   - TIE
        "C": 2 + 0      # Opponent: Scissor - LOSS
    },
    "Z": {          # Player: SCISSOR
        "A": 3 + 0,     # Opponent: Rock    - LOSS
        "B": 3 + 6,     # Opponent: Paper   - WIN
        "C": 3 + 3      # Opponent: Scissor - TIE
    }
}

score = 0

for line in game_input:
    opponent = line.split()[0]
    player = line.split()[1]
    score += lookup[player][opponent]

print(score)
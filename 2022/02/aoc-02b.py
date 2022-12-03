#!/usr/bin/env python3
# Advent of Code 2022: Day 2 (part 2)
# Submission by qxtal <quartz@xtal.sh>

f = open('./input.txt', 'r')
game_input = f.readlines()
f.close()

# This can definitely be done in a better way, but it works.
lookup = {
    "X": {          # Player: Needs to LOSE
        "A": 3 + 0,     # Opponent: Rock    - Player pick: Scissor
        "B": 1 + 0,     # Opponent: Paper   - Player pick: Rock
        "C": 2 + 0      # Opponent: Scissor - Player pick: Paper
    },
    "Y": {          # Player: Needs to TIE
        "A": 1 + 3,     # Opponent: Rock    - Player pick: Rock
        "B": 2 + 3,     # Opponent: Paper   - Player pick: Paper
        "C": 3 + 3      # Opponent: Scissor - Player pick: Scissor
    },
    "Z": {          # Player: Needs to WIN
        "A": 2 + 6,     # Opponent: Rock    - Player pick: Paper
        "B": 3 + 6,     # Opponent: Paper   - Player pick: Scissor
        "C": 1 + 6      # Opponent: Scissor - Player pick: Rock
    }
}

score = 0

for line in game_input:
    opponent = line.split()[0]
    player = line.split()[1]
    score += lookup[player][opponent]

print(score)
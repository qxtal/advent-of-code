#!/usr/bin/env python3
# Advent of Code 2022: Day 3 (part 2)
# Submission by qxtal <quartz@xtal.sh>

f = open('./input.txt', 'r')
rucksack_input = f.readlines()
f.close()

count = 0

for x in range(0, len(rucksack_input), 3):
    group1 = rucksack_input[x].strip()
    group2 = rucksack_input[x+1].strip()
    group3 = rucksack_input[x+2].strip()

    for item in group1:
        if item in group2 and item in group3:
            if item.islower():
                count += ord(item) - 96 # ASCII offset
            else:
                count += (ord(item) - 64) + 26 # ASCII offset + priority
            break # to avoid duplicates

print(count)
#!/usr/bin/env python3
# Advent of Code 2022: Day 3 (part 1)
# Submission by qxtal <quartz@xtal.sh>

f = open('./input.txt', 'r')
rucksack_input = f.readlines()
f.close()

count = 0
    
for line in rucksack_input:
    cmp1 = line[:len(line)//2]
    cmp2 = line[len(line)//2:]
    
    for item in cmp1:
        if item in cmp2:
            if item.islower():
                count += ord(item) - 96 # ASCII offset
            else:
                count += (ord(item) - 64) + 26 # ASCII offset + priority
            break # to avoid duplicates

print(count)
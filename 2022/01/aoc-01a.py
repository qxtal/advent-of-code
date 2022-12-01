#!/usr/bin/env python3
# Advent of Code 2022: Day 1 (part 1)
# Submission by qxtal <quartz@xtal.sh>

f = open('./input.txt', 'r') # hard-coded input file ¯\_(ツ)_/¯
elf_input = f.readlines()
f.close()

elf_calories = [0] # first element initialized with zero

for line in elf_input:
    if line.strip().isdigit():
        elf_calories[-1] += int(line)
    else:
        elf_calories.append(0) # add new element, init with zero

elf_calories.sort(reverse=True)
top_calories = elf_calories[0]

print(top_calories)

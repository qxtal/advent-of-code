#!/usr/bin/env python3
# Advent of Code 2022: Day 4 (part 1)
# Submission by qxtal <quartz@xtal.sh>

# Thanks to @polaak@mstdn.social for helping me with
# a frustrating bug that had me stuck for a while!
# Remember to convert your values to ints!

f = open('./input.txt', 'r')
cleanup_input = f.readlines()
f.close()

count = 0

for line in cleanup_input:
    pair1 = line.strip().split(",")[0].split("-")
    pair2 = line.strip().split(",")[1].split("-")
    
    p1x, p1y = int(pair1[0]), int(pair1[1])
    p2x, p2y = int(pair2[0]), int(pair2[1])
    
    if (p1x <= p2x and p1y >= p2y
        or p1x >= p2x and p1y <= p2y):
        count += 1

print(count)

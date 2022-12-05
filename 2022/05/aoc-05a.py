#!/usr/bin/env python3
# Advent of Code 2022: Day 5 (part 1)
# Submission by qxtal <quartz@xtal.sh>

def parse_crates_to_stacks(cr_input):        
    x_length = len(cr_input[-1].replace(" ", "").strip())
    y_length = len(cr_input)
    
    crate_stacks = []
    for x in range(1, x_length * 4, 4):
        stack = []
        for y in range(y_length - 2, -1, -1):
            c = cr_input[y][x]
            if c.isalpha():
                stack.append(cr_input[y][x])
        crate_stacks.append(stack)

    return crate_stacks

def main():
    f = open('./input.txt', 'r')
    crates_input = f.readlines()
    f.close()

    crates = parse_crates_to_stacks(crates_input[:9])
    
    for line in crates_input[10::]:
        (c_amount, c_from, c_to) = [int(n) for n in line.split()[1::2]]
        for _ in range(c_amount):
            crates[c_to - 1].append(crates[c_from - 1].pop())
    
    result = ""
    for stack in crates:
        result += stack[-1]
    
    print(result)
    
if __name__ == "__main__":
    main()

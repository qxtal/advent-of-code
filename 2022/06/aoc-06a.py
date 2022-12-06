#!/usr/bin/env python3
# Advent of Code 2022: Day 6 (part 1)
# Submission by qxtal <quartz@xtal.sh>

def main():
    f = open('./input.txt', 'r')
    stream = f.readlines()[0]
    f.close() 
    
    result = ""
    
    for i in range(0, len(stream) - 4):
        chunk = stream[i:i + 4]
        if len(set(chunk)) == len(chunk):
            result = i + 4
            break
    
    print(result)
    
if __name__ == "__main__":
    main()

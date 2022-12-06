#!/usr/bin/env python3
# Advent of Code 2022: Day 6 (part 2)
# Submission by qxtal <quartz@xtal.sh>

def main():
    f = open('./input.txt', 'r')
    stream = f.readlines()[0]
    f.close() 
    
    result = ""
    
    for i in range(0, len(stream) - 14):
        chunk = stream[i:i + 14]
        if len(set(chunk)) == len(chunk):
            result = i + 14
            break
    
    print(result)
    
if __name__ == "__main__":
    main()

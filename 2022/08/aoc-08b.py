#!/usr/bin/env python3
# Advent of Code 2022: Day 8 (part 1)
# Submission by qxtal <quartz@xtal.sh>

def main():
    f = open('./input.txt', 'r')
    trees_input = f.readlines()
    f.close() 
    
    tree_map = []
    scenic_high_score = 0
    
    for line in trees_input:
        tree_map.append(list(map(int,line.strip())))
    
    for row_idx, row in enumerate(tree_map):
        if row_idx == 0 or row_idx == len(tree_map) - 1:
            continue
        for col_idx, column in enumerate(row):
            if col_idx == 0 or col_idx == len(row) - 1:
                continue
            else:
                current_tree_height = column
                current_tree_scenic_score = 0
                
                v_up = 0
                v_down = 0
                v_left = 0
                v_right = 0
                
                for left in range(col_idx - 1, -1, -1):
                    comp_left = tree_map[row_idx][left]
                    if current_tree_height <= comp_left:
                        v_left += 1
                        break
                    else:
                        v_left += 1
                    
                for right in range(col_idx + 1, len(row), 1):
                    comp_right = tree_map[row_idx][right]
                    if current_tree_height <= comp_right:
                        v_right += 1
                        break
                    else:
                        v_right += 1

                for up in range(row_idx - 1, -1, -1):
                    comp_up = tree_map[up][col_idx]
                    if current_tree_height <= comp_up:
                        v_up += 1
                        break
                    else:
                        v_up += 1
                
                for down in range(row_idx + 1, len(tree_map), 1):
                    comp_down = tree_map[down][col_idx]
                    if current_tree_height <= comp_down:
                        v_down += 1
                        break
                    else:
                        v_down += 1

                current_tree_scenic_score = v_up * v_down * v_left * v_right
                
                if scenic_high_score <= current_tree_scenic_score:
                    scenic_high_score = current_tree_scenic_score
        
    print(scenic_high_score)
    
if __name__ == "__main__":
    main()

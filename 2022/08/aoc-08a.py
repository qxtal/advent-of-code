#!/usr/bin/env python3
# Advent of Code 2022: Day 8 (part 1)
# Submission by qxtal <quartz@xtal.sh>

def main():
    f = open('./input.txt', 'r')
    trees_input = f.readlines()
    f.close() 
    
    tree_map = []
    visible_trees = 0
    
    for line in trees_input:
        tree_map.append(list(map(int,line.strip())))
    
    for row_idx, row in enumerate(tree_map):
        if row_idx == 0 or row_idx == len(tree_map) - 1:
            visible_trees += len(row)
            continue
        
        for col_idx, column in enumerate(row):
            if col_idx == 0 or col_idx == len(row) - 1:
                visible_trees += 1
            else:
                current_tree_height = column
                blocked = 0
                
                for left in range(0, col_idx, 1):
                    comp_left = tree_map[row_idx][left]
                    if current_tree_height <= comp_left:
                        blocked += 1
                        break
                    
                for right in range(len(row) - 1, col_idx, -1):
                    comp_right = tree_map[row_idx][right]
                    if current_tree_height <= comp_right:
                        blocked += 1
                        break
                    
                for up in range(0, row_idx, 1):
                    comp_up = tree_map[up][col_idx]
                    if current_tree_height <= comp_up:
                        blocked += 1
                        break
                
                for down in range(len(tree_map) - 1, row_idx, -1):
                    comp_down = tree_map[down][col_idx]
                    if current_tree_height <= comp_down:
                        blocked += 1
                        break
                
                if blocked < 4:
                    visible_trees += 1
        
    print(visible_trees)
    
if __name__ == "__main__":
    main()

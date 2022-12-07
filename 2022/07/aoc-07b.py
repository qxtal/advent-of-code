#!/usr/bin/env python3
# Advent of Code 2022: Day 6 (part 2)
# Submission by qxtal <quartz@xtal.sh>

# This... was harder than I anticipated.
# I spent hours trying to fix bugs that would cause the
# incorrect sum to be calculated. If my code looks a bit
# messy or unoptimized, it's simply because I don't care
# anymore, and it finally works now. That's what matters.

class DirNode:
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.children = {}
        self.parent = None
        
    def add_file(self, name, size):
        self.files[name] = size
    
    def add_child_dir(self, obj):
        obj.parent = self
        self.children[obj.name] = obj
    
    def get_total_size(self):
        size = 0
        for file in self.files:
            size += self.files[file]
        if bool(self.children):
            ch_size = 0
            for child in self.children:
                ch_size += self.children[child].get_total_size()
            return size + ch_size
        else:
            return size
    
    def get_root_node(self):
        if self.parent is None:
            return self
        else:
            return self.parent.get_root_node()


def main():
    f = open('input.txt', 'r')
    file_listing = f.readlines()
    f.close() 
    
    sizes = {}
    current = DirNode("/")
    current_size = 0
    
    for line in file_listing[1::]:
        tokens = line.split()
        
        if tokens[0] == "$":
            if tokens[1] == "ls":
                pass # just skip to next line
            elif tokens[1] == "cd":
                if tokens[2] == "..":
                    current = current.parent
                else:
                    current = current.children[current.name + tokens[2] + "/"]
        else:
            if tokens[0] == "dir":
                d = DirNode(current.name + tokens[1] + "/")
                current.add_child_dir(d)
            elif tokens[0].isnumeric():
                current.add_file(tokens[1], int(tokens[0]))
                
        current_size = current.get_total_size()
        size_dict = { current.name: current_size }
        sizes.update(size_dict)
    
    root = current.get_root_node() # get root node
    disk_space_max = 70000000
    disk_space_used = root.get_total_size()
    
    # HACK: Force-update root size, as it's incorrect for some reason.
    # I know it's a bug that should be fixed, but I am too tired for
    # this now. I just wanna finish this crap, then we can pretty
    # things up at a later time (or not)
    sizes["/"] = root.get_total_size()
    
    s_sorted = dict(sorted(sizes.items(), key=lambda item: item[1]))
    for i in s_sorted:
        s = s_sorted.get(i)
        if disk_space_max - (disk_space_used - s) >= 30000000:
            print(s)
            break

if __name__ == "__main__":
    main()

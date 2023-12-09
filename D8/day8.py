import re
import numpy as np
# Part one

def part_one():
    a = list(open("input"))
    dirs = {}
    for line in a[2:]:
        f,l,r = re.sub("[()=,]", "", line).split()
        dirs[f] = {"R":r,"L":l}
    pointer = "AAA"
    steps = 0
    instructions = a[0].strip()
    while pointer != "ZZZ":
        pointer = dirs[pointer][instructions[steps%len(instructions)]]
        steps += 1
    print(steps)

def part_two():
    a = list(open("input"))
    dirs = {}
    for line in a[2:]:
        f,l,r = re.sub("[()=,]", "", line).split()
        dirs[f] = {"R":r,"L":l}
    pointers = [x for x in dirs.keys() if x[-1]=="A"]
    pos = []

    instructions = a[0].strip()
    for pointer in pointers:
        # Steps from A to Z
        steps = 0
        while pointer[-1] != "Z":
            pointer = dirs[pointer][instructions[steps % len(instructions)]]
            steps += 1
        pos.append(steps)
    print(pos[0],np.lcm.reduce(np.array(pos,dtype=np.int64)))

#part_one()
part_two()
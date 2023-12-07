# Sol Steele
import numpy as np

def part_one():
    dirs = np.array([(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)])
    total = 0
    with open("input") as f:
        a = np.array([list(a.strip("\n")) for a in list(f)])
        for r, line in enumerate(a):
            n = []
            num = ""
            for c, char in enumerate(line):
                if char.isdigit():
                    num += char
                    n += [a[y,x] for x, y in dirs+[c,r] if 0 <= x < len(a[0]) and 0 <= y < len(a)]
                else:
                    if num != "" and (np.array([x not in "1234567890." for x in n])).any():
                        total += int(num)
                    num = ""
                    n = []
            if num != "" and (np.array([x not in "1234567890." for x in n])).any():
                total += int(num)

    print(total)

def part_two():
    dirs = np.array([(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)])
    with open("test") as f:
        a = np.array([list(a.strip("\n")) for a in list(f)])

    numbers = []
    for r, line in enumerate(a):
        num = ""
        locs = []
        for c, char in enumerate(line):
            if char.isdigit():
                locs.append([r,c])
                num += char
            elif num != "":
                numbers.append([int(num), set([tuple(x) for x in locs])])
                locs = []
                num = ""
        if num != "":
            numbers.append([int(num), set([tuple(x) for x in locs])])


    total = 0
    for cog in np.array(np.where(a == "*")).T:
        cog_dirs = set([tuple(x) for x in dirs+cog])
        n = [x[0] for x in numbers if len(cog_dirs.intersection(x[1])) > 0]
        total += np.prod(n) * (len(n) == 2)
    print(total)




part_one()
part_two()

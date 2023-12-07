import numpy as np


def part_one():
    hands = []
    for line in list(open("input")):
        h, b = line.split()
        for a in ["Kk","Ax","TC"]:
            h = h.replace(*a)
        _, c = np.unique(list(h), return_counts=True)
        c.sort()
        if c[-1] == 5: h = "9" + h
        elif c[-1] == 4: h = "8" + h
        elif c[-1] == 3 and c[-2] == 2: h = "7" + h
        elif c[-1] == 3: h = "6" + h
        elif c[-1] == 2 and c[-2] == 2: h = "5" + h
        elif c[-1] == 2: h = "4" + h
        else: h = "3" + h
        hands.append([h, b])
    hands.sort(key=lambda x: x[0])
    print(sum([int(c[1]) * (i + 1) for i, c in enumerate(hands)]))


def part_two():
    hands = []
    for line in list(open("input")):
        h, b = line.split()
        for a in ["Kk","Ax","TC","J0"]:
            h = h.replace(*a)
        j = h.count("0")
        _, c = np.unique(list(h.replace("0","")), return_counts=True)
        c.sort()
        if j == 5 or c[-1]+j == 5: h = "9" + h
        elif c[-1]+j == 4: h = "8" + h
        elif c[-1]+j == 3 and c[-2] == 2: h = "7" + h
        elif c[-1]+j == 3: h = "6" + h
        elif c[-1]+j == 2 and c[-2] == 2: h = "5" + h
        elif c[-1]+j == 2: h = "4" + h
        else: h = "3" + h
        hands.append([h, b])
    hands.sort(key=lambda x: x[0])
    print(sum([int(c[1]) * (i + 1) for i, c in enumerate(hands)]))


def part_a(s):
    hands = []
    for line in list(open("input")):
        h, b = line.split()
        for a in ["Kk","Ax","TC","J"+s]:
            h = h.replace(*a)
        j = h.count("0") * (s=="0")
        _, c = np.unique(list(h.replace("0","")), return_counts=True)
        c.sort()
        if j == 5 or c[-1]+j == 5: h = "9" + h
        elif c[-1]+j == 4: h = "8" + h
        elif c[-1]+j == 3 and c[-2] == 2: h = "7" + h
        elif c[-1]+j == 3: h = "6" + h
        elif c[-1]+j == 2 and c[-2] == 2: h = "5" + h
        elif c[-1]+j == 2: h = "4" + h
        else: h = "3" + h
        hands.append([h, b])
    hands.sort(key=lambda x: x[0])
    print(sum([int(c[1]) * (i + 1) for i, c in enumerate(hands)]))


part_one()
part_two()
part_a("J")
part_a("0")

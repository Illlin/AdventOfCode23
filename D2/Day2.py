# Sol Steele
import re
import numpy as np

def part_one():
    total = 0
    maxes = {"red": 12, "green": 13, "blue": 14}
    with open("input") as f:
        for i, line in enumerate(f):
            possible = True
            for hand in line.split(":")[1].split(";"):
                for cube in hand.split(","):
                    number = int(re.sub("\\D", "", cube))
                    for colour in maxes:
                        if colour in cube:
                            if number > maxes[colour]:
                                possible = False
            if possible:
                total += i+1
    print(total)

def part_two():
    with open("input") as f:
        total = 0
        for line in f:
            mins = {"red": 0, "green": 0, "blue": 0}
            for hand in line[:-1].split(":")[1].split(";"):
                for cube in hand.split(","):
                    number = int(re.sub("\\D", "", cube))
                    mins[cube.split(" ")[-1]] = max(number, mins[cube.split(" ")[-1]])
            total += np.prod(list(mins.values()))
        print(total)


part_one()
part_two()

import numpy as np
import itertools
def part_one():
    a = np.array([[*a.strip()] for a in [*open("input")]])
    a = a[np.sort(np.concatenate((np.arange(len(a)), np.where((a == ".").all(axis=1))[0])))]
    a = a.T[np.sort(np.concatenate((np.arange(len(a.T)), np.where((a.T == ".").all(axis=1))[0])))].T
    a = np.dstack(np.where(a == ["#"]))[0]
    i, j = np.split(np.array([*itertools.combinations(a, 2)]), 2, axis=1)
    print(np.sum(abs(i - j)))

def part_two():
    a = np.array([[*a.strip()] for a in [*open("test")]])
    a = a == "#"
    # Calculate Height
    b = a[np.sort(np.concatenate((np.arange(len(a)), np.repeat(np.where((a == False).all(axis=1))[0],1))))]
    b = np.where(b)[0]
    # Calculate width
    c = a.T[np.sort(np.concatenate((np.arange(len(a.T)), np.repeat(np.where((a.T == False).all(axis=1))[0],1))))].T
    c = np.where(c)[0]
    a = np.dstack([b,c])
    i, j = np.split(np.array([*itertools.combinations(a, 2)]), 2, axis=1)
    print(np.sum(abs(i - j)))

def part_two_better(z):
    a = [[b=="." for b in a.strip()] for a in [*open("input")]]
    row_cost,col_cost = [[1+z*all(b) for b in c] for c in [a,zip(*a)]]
    f = [i for l in a for i in l]
    w = len(a[0])
    i = [x for x in range((len(f))) if not f[x]]
    print(sum([sum(col_cost[x%w+1:y%w+1]+col_cost[y%w+1:x%w+1]+row_cost[x//w+1:y//w+1]+row_cost[y//w+1:x//w+1]) for x,y in itertools.combinations(i,2)]))
part_two_better(1)
part_two_better(999999)
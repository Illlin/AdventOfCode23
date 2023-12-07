import numpy as np
import time
import timeit

def part_one():
    t, d = np.array([a.split()[1:] for a in list(open("input"))], dtype=np.int64)
    print(np.prod([sum((np.arange(c) * (c - np.arange(c))) > d[i]) for i, c in enumerate(t)]))

def part_two():
    t,d = [int("".join([x for x in b.split(":")[1] if x.isdigit()])) for b in list(open("input"))]
    print(sum((np.arange(t,dtype=np.int64) * (t-np.arange(t,dtype=np.int64))) > d))

a=time.perf_counter_ns()
part_one()
print(time.perf_counter_ns()-a)

part_two()
import numpy as np

map = np.array([[int(y) for y in x.strip()] for x in open("input")])
goal = len(map) - 1
best = 100000

history = {}
start_cost = map[0,0]
to_check = [
    [-start_cost, np.array([0, 0]), np.array([0, 1]), 0],
    [-start_cost, np.array([0, 0]), np.array([1, 0]), 0]
]

while len(to_check):
    # get lowest t
    sm = to_check[0][0]
    smi = 0
    for i, c in enumerate(to_check):
        if c[0] < sm:
            smi = i
            sm = c[0]

    t, pos, d, s = to_check[smi]
    del to_check[smi]

    if not (all(0 <= pos) and all(pos <= goal)):
        continue
    t = t + map[*pos]
    if s > 8:
        continue
    if t >= best:
        continue
    if all(pos == goal) and s > 2:  # Have I made it?
        print(t)
        best = t

    # Check if I have been here before but better
    # Location hash
    h = pos[0] * 10000000 + pos[1] * 10000 + (d[0] + 2) * 1000 + (d[1] + 2) * 100 + s + 1

    if h in history:
        if history[h] <= t:
            continue
    history[h] = t

    to_check.append([t, pos + d, d, s + 1])

    if s > 2:
        for i in range(8):
            history[h+1] = t

        a = np.array([d[1], d[0]])
        to_check.append([t, pos + a, a, 0])
        a = np.array([-d[1], -d[0]])
        to_check.append([t, pos + a, a, 0])


pass


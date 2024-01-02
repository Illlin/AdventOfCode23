import numpy as np

map = np.array([[int(y) for y in x.strip()] for x in open("input")])
goal = len(map) - 1
best = 100000

history = {}


def step(t, pos, d, s):
    global best
    if not (all(0 <= pos) and all(pos <= goal)):
        return
    t = t + map[*pos]
    if s > 2:
        return
    if t >= best:
        return
    if all(pos == goal):  # Have I made it?
        print(t)
        best = t

    # Check if I have been here before but better
    # Location hash
    h = pos[0] * 10000000 + pos[1] * 10000 + (d[0] + 2) * 1000 + (d[1] + 2) * 100 + s + 1

    if h in history:
        if history[h] <= t:
            return
    history[h] = t
    history[h + 1] = t
    history[h + 2] = t

    step(t, pos + d, d, s + 1)

    a = np.array([d[1], d[0]])
    step(t, pos + a, a, 0)
    a = np.array([-d[1], -d[0]])
    step(t, pos + a, a, 0)

start_cost = map[0,0]
step(-start_cost, np.array([0, 0]), np.array([0, 1]), 0)
step(-start_cost, np.array([0, 0]), np.array([1, 0]), 0)

pass


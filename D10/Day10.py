import numpy as np
a = np.array([[*x.strip()] for x in [*open("input")]])
maze = np.zeros(a.shape)
nest = np.zeros(a.shape,dtype=str)
s_point = np.dstack(np.where(a=="S"))[0,0]
direction = ""
w = len(a[0])-1
if a[*s_point-[1,0]] in "7|F":
    direction = "u"
if a[*s_point+[1,0]] in "J|L":
    direction = "d"
if a[*s_point-[0,1]] in "L-F":
    direction = "l"
if a[*s_point+[0,1]] in "J-7":
    direction = "r"
print(direction)
point = np.copy(s_point)
steps = 0
nest[*point] = a[*point]
while True:
    steps += 1
    if direction == "u":
        point -= [1, 0]
        maze[*point] = steps
        if a[*point] == "S":
            break
        if a[*point] == "7":
            direction = "l"
        if a[*point] == "F":
            direction = "r"
    elif direction == "d":
        point += [1, 0]
        maze[*point] = steps
        if a[*point] == "S":
            break
        if a[*point] == "J":
            direction = "l"
        if a[*point] == "L":
            direction = "r"
    elif direction == "l":
        point -= [0, 1]
        maze[*point] = steps
        if a[*point] == "S":
            break
        if a[*point] == "L":
            direction = "u"
        if a[*point] == "F":
            direction = "d"
    elif direction == "r":
        point += [0, 1]
        maze[*point] = steps
        if a[*point] == "S":
            break
        if a[*point] == "J":
            direction = "u"
        if a[*point] == "7":
            direction = "d"
    nest[*point] = a[*point]
print(np.max(maze)//2)


direction = ""
if a[*s_point-[1,0]] in "7|F":
    direction = "u"
if a[*s_point+[1,0]] in "J|L":
    direction = "d"
if a[*s_point-[0,1]] in "L-F":
    direction = "l"
if a[*s_point+[0,1]] in "J-7":
    direction = "r"
print(direction)
point = np.copy(s_point)
filling = np.zeros(a.shape)
filling[*point] = -1
while True:
    steps += 1
    if direction == "u":
        # set Fill
        if nest[*np.clip(point - [0, 1], 0, w)] == "":
            filling[*point - [0, 1]] = 1
        if nest[*np.clip(point + [0, 1], 0, w)] == "":
            filling[*point + [0, 1]] = 2

        point -= [1, 0]
        maze[*point] = steps
        if a[*point] == "S":
            break
        if a[*point] == "7":
            direction = "l"
        if a[*point] == "F":
            direction = "r"
    elif direction == "d":
        # set Fill
        if nest[*np.clip(point + [0, 1], 0, w)] == "":
            filling[*point + [0, 1]] = 1
        if nest[*np.clip(point - [0, 1], 0, w)] == "":
            filling[*point - [0, 1]] = 2

        point += [1, 0]
        maze[*point] = steps
        if a[*point] == "S":
            break
        if a[*point] == "J":
            direction = "l"
        if a[*point] == "L":
            direction = "r"
    elif direction == "l":
        # set Fill
        if nest[*np.clip(point + [1, 0], 0, w)] == "":
            filling[*point + [1, 0]] = 1
        if nest[*np.clip(point - [1, 0], 0, w)] == "":
            filling[*point - [1, 0]] = 2

        point -= [0, 1]
        maze[*point] = steps
        if a[*point] == "S":
            break
        if a[*point] == "L":
            direction = "u"
        if a[*point] == "F":
            direction = "d"
    elif direction == "r":
        # set Fill
        if nest[*np.clip(point - [1, 0], 0, w)] == "":
            filling[*point - [1, 0]] = 1
        if nest[*np.clip(point + [1, 0], 0, w)] == "":
            filling[*point + [1, 0]] = 2

        point += [0, 1]
        maze[*point] = steps
        if a[*point] == "S":
            break
        if a[*point] == "J":
            direction = "u"
        if a[*point] == "7":
            direction = "d"
    filling[*point] = -1

for _ in range(50):
    for i in range(w+1):
        for j in range(w+1):
            if filling[i,j] == 0:
                p = [
                    filling[i, np.clip(j + 1, 0, w)],
                    filling[i, np.clip(j - 1, 0, w)],
                    filling[np.clip(i + 1, 0, w), j],
                    filling[np.clip(i - 1, 0, w), j],
                    0
                ]
                filling[i,j] = max(p)



for i in filling:
    for j in i:
        if j == 0: print("?",end="")
        elif j == -1: print("-",end="")
        elif j == 1: print("~",end="")
        elif j == 2: print("O",end="")
        #else: print(j,end="")
    print("")
pass
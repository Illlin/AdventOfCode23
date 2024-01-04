import numpy as np
coms = [a.split() for a in open("test")]

point = np.array([0,0])
dirs = {
    "U": np.array([0, 1]),
    "D": np.array([0, -1]),
    "R": np.array([1, 0]),
    "L": np.array([-1, 0]),
}
inside = {
    "U": np.array([1,0]),
    "D": np.array([-1,0]),
    "R": np.array([0,-1]),
    "L": np.array([0,1])
}
# Load coms from hex
hexLoad = {
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U",
}
coms = [[hexLoad[a[2].strip("(#)")[-1]],int(a[2].strip("(#)")[:-1],16)] for a in coms]
#coms = [[x[0], int(x[1])] for x in coms]


x = []
y = []
points = []
# generate list of needed coords
for i in coms:
    x.append(point[0])
    #x.append(point[0] - 1)
    x.append(point[0] + 1)
    y.append(point[1])
    #y.append(point[1] - 1)
    y.append(point[1] + 1)
    points.append([point[0],point[1], i[0]])
    point += dirs[i[0]]*i[1]
points.append([point[0],point[1], i[0]])
x = np.array(sorted(set(x)))
y = np.array(sorted(set(y)))


zone = np.ones((len(x), len(y)))
p = points[0]
for goal in points[0:]:
    while (p[0] != goal[0]) or (p[1] != goal[1]):
        p_index = (np.where(x == p[0])[0][0], np.where(y == p[1])[0][0])
        zone[*p_index] = 0
        if zone[*(inside[p[2]]+p_index)] == 1:
            zone[*(inside[p[2]]+p_index)] = -1
        p[0] = x[p_index[0]+dirs[p[2]][0]]
        p[1] = y[p_index[1]+dirs[p[2]][1]]
    p[2] = goal[2]
    pass

d = np.array(list(dirs.values()))
for t in range(100):
    print("\r",t,end="")
    for a in range(min(zone.shape)-1):
        for _ in range(4):
            zone[a] = np.where((zone[a] == 1) & (zone[a+1] == [-1]), -1, zone[a])
            zone=np.rot90(zone)

print("Printing")
for line in zone:
    for char in line:
        if char == 0:
            print("+",end="")
        elif char == 1:
            print(" ",end="")
        elif char == -1:
            print("~",end="")
        else:
            print("@",end="")
    print()

zone = zone!=1
xp = list(x) + [max(x)+1]
yp = list(y) + [max(y)+1]
xv = np.array([xp[i+1]-c for i,c in enumerate(x)])
yv = np.array([yp[i+1]-c for i,c in enumerate(y)])
values = xv.reshape(1,-1)*yv.reshape(-1,1)
print(np.sum((yv.reshape(1,-1).astype(np.int64)*xv.reshape(-1,1))*zone))
pass

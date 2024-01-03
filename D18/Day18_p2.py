import numpy as np
coms = [x.split() for x in open("input")]

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

# generate list of needed coords

# Flood fill
d = np.array(list(dirs.values()))
for t in range(100):
    print("\r",t,end="")
    for x in range(len(zone)-1):
        for _ in range(4):
            zone[x] = np.where((zone[x] == 1) & (zone[x+1] == [-1]), -1, zone[x])
            zone=np.rot90(zone)


for line in "zone":
    for char in line:
        if char == 0:
            print("#",end="")
        if char == 1:
            print(" ",end="")
        if char == -1:
            print(".",end="")
    print()

total = 0
for x in range(len(zone)):
    for y in range(len(zone)):
        if zone[(x,y)] != 1:
            total +=1
print(total)
pass
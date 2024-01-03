import numpy as np
coms = [x.split() for x in open("input")]
size = 1024
zone = np.ones([size, size])

point = np.array([int(size/2), int(size/2)])
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
right_wall = True
# Generate border
for com in coms:
    for i in range(int(com[1])):
        zone[*point] = 0
        # Fill inside
        zone[*(point+inside[com[0]])] *= -1
        point += dirs[com[0]]

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
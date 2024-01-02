import numpy as np
map = np.array([[*x.strip()] for x in open("input")])

seen_beams = []
beams = [[(0, 0), (0, 1)]]

while len(beams):
    print(beams)
    b = beams.pop()

    if 0 <= b[0][0] < map.shape[0] and 0 <= b[0][1] < map.shape[1]:
        if b in seen_beams:
            print("Beam Repeat")
            continue
        else:
            seen_beams.append(b)

        if map[b[0]] == ".":
            # Continue
            beams.append([(b[0][0]+b[1][0], b[0][1]+b[1][1]), b[1]])

        elif map[b[0]] == "|":
            if b[1][1] != 0:
                # Split
                beams.append([(b[0][0] + 1, b[0][1]), (+1, 0)])
                beams.append([(b[0][0] - 1, b[0][1]), (-1, 0)])
            else:
                # Continue
                beams.append([(b[0][0] + b[1][0], b[0][1] + b[1][1]), b[1]])

        elif map[b[0]] == "-":
            if b[1][0] != 0:
                # Split
                beams.append([(b[0][0], b[0][1] + 1), (0, +1)])
                beams.append([(b[0][0], b[0][1] - 1), (0, -1)])
            else:
                # Continue
                beams.append([(b[0][0] + b[1][0], b[0][1] + b[1][1]), b[1]])

        elif map[b[0]] == "/":
            dir = (-b[1][1], -b[1][0])
            beams.append([(b[0][0]+dir[0],b[0][1]+dir[1]),dir])

        elif map[b[0]] == "\\":
            dir = (b[1][1], b[1][0])
            beams.append([(b[0][0]+dir[0],b[0][1]+dir[1]),dir])

        else:
            print("Unknown symbol", map[b[0]])
            break
    else:
        print("Beam",b,"Exit")

print("Tiles visited")
print(len(set([x[0] for x in seen_beams])))
pass
import numpy as np
map = np.array([[*x.strip()] for x in open("input")])

best = 0

for i in range(4):
    for j in range(len(map)):
        seen_beams = []

        if i == 0:
            beams = [[(j, 0), (0, 1)]]
        if i == 1:
            beams = [[(j, len(map)-1), (0, -1)]]
        if i == 2:
            beams = [[(0, j), (1, 0)]]
        if i == 3:
            beams = [[(len(map)-1, j), (-1, 0)]]

        while len(beams):
            b = beams.pop()

            if 0 <= b[0][0] < map.shape[0] and 0 <= b[0][1] < map.shape[1]:
                if b in seen_beams:
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
                pass

        hot = len(set([x[0] for x in seen_beams]))
        print("Tiles visited", hot)
        best = max(best, hot)

print("Hottest:",best)
pass
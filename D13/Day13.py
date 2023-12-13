a = list(open("input"))
a.append("\n")

land = []
t = 0
for line in a:
    if line == "\n":
        pass
        # Step one, check horizontal
        for i in range(len(land)-1):
            smudges = 0
            valid = True
            for j in range(0,i+1):
                if 0 <= i-j and i+j+1 < len(land):
                    if land[i-j] != land[i+j+1]:
                        valid = False
                        break
            if valid:
                t += 100*(i+1)
                print(100*(i+1))
                break
        if not valid:
            # Transpose and try again!
            land = [x.strip() for x in land]
            land = ["".join(x) for x in zip(*land)]
            # Step Two, check horizontal
            for i in range(len(land) - 1):
                valid = True
                for j in range(0, i + 1):
                    if 0 <= i - j and i + j + 1 < len(land):
                        if land[i - j] != land[i + j + 1]:
                            valid = False
                            break
                if valid:
                    print(i+1)
                    t += i+1
                    break
            if not valid:
                print("No mirror found!")

        land = []
    else:
        land.append(line)

print(t)

# PART TWO
print("\n\n PART TWO \n\n")

a = list(open("input"))
a.append("\n")

land = []
t = 0
for line in a:
    if line == "\n":
        pass
        # Step one, check horizontal
        valid = False
        for i in range(len(land)-1):
            smudges = 0
            for j in range(0,i+1):
                if 0 <= i-j and i+j+1 < len(land):
                    a = land[i-j]
                    b = land[i+j+1]
                    smudges += sum(1 for a, b in zip(a, b) if a != b)
            if smudges == 1:
                valid = True
                t += 100*(i+1)
                print(100*(i+1))
                break
        if not valid:
            # Transpose and try again!
            valid = True
            land = [x.strip() for x in land]
            land = ["".join(x) for x in zip(*land)]
            # Step Two, check horizontal
            for i in range(len(land) - 1):
                smudges = 0
                for j in range(0, i + 1):
                    if 0 <= i - j and i + j + 1 < len(land):
                        a = land[i - j]
                        b = land[i + j + 1]
                        smudges += sum(1 for a, b in zip(a, b) if a != b)
                if smudges == 1:
                    valid = False
                    print(i+1)
                    t += i+1
                    break
            if not valid:
                print("No mirror found!")

        land = []
    else:
        land.append(line)

print(t)
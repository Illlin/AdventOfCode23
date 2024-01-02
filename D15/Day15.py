def c_hash(string):
    total = 0
    for char in string:
        total += ord(char)
        total *= 17
        total %= 256
    return total

a = list(open("input"))[0].strip().split(",")
print(sum([c_hash(x) for x in a]))

boxes = {}
for i in range(256):
    boxes[i] = []

for i in a:
    if i[-1] == "-":
        name = i[:-1]
        box = c_hash(name)

        found = -1
        for j in range(len(boxes[box])):
            if boxes[box][j][0] == name:
                found = j
        if found >= 0:
            del boxes[box][found]

        pass
    elif i[-2] == "=":
        name = i[:-2]
        power = int(i[-1])
        box = c_hash(name)

        found = False
        for j in range(len(boxes[box])):
            if boxes[box][j][0] == name:
                boxes[box][j][1] = power
                found = True
        if not found:
            boxes[box].append([name, power])
    pass

total = 0
for box in boxes:
    for i, lense in enumerate(boxes[box]):
        total += (box+1)*(i+1)*lense[1]
print(total)
pass
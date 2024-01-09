a = list(open("input"))
parts = {"button": ["b", ["roadcaster"]]}

for line in a:
    b = line.split()
    parts[b[0][1:]] = [b[0][0], [x.strip(",") for x in b[2:]]]

# Get inverse connection map
inverse = {x: [] for x in parts.keys()}
for gate in parts:
    for i in parts[gate][1]:
        if i in inverse:
            inverse[i].append(gate)

# generate memory
memory = {}
for gate in parts:
    if parts[gate][0] == "%":
        memory[gate] = 0
    if parts[gate][0] == "&":
        memory[gate] = {x: 0 for x in inverse[gate]}
count = 0
for i in range(100000):
    props = [["button", 0, "roadcaster"]]
    count += 1
    while len(props) > 0:
        f, s, d = props[0]
        props = props[1:]
        if d == "rx" and s == 0:
                print(c)
        if d not in parts:
            continue
        if parts[d][0] == "b":
            # Broadcaster
            for c in parts[d][1]:
                props.append([d, s, c])
        elif parts[d][0] == "%":
            # Flip Flop
            if s == 0:
                memory[d] = int(not memory[d])
                for c in parts[d][1]:
                    props.append([d, memory[d], c])
        elif parts[d][0] == "&":
            # Conjunction
            memory[d][f] = s
            for c in parts[d][1]:
                props.append([d, int(not all(memory[d].values())), c])

print(sigs[0] * sigs[1])

pass

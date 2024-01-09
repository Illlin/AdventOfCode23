parts = []
processes = {"A": "A", "R": "R"}
for line in open("test"):
    if line == "\n":
        continue
    if "=" in line:
        parts.append({a[0]: int(a[1]) for a in [x.split("=") for x in line.strip("{\n}").split(",")]})
    else:
        a,b = line.strip().split("{")
        processes[a] = b[:-1]
pass

def run_process(item, process):
    for step in process.split(","):
        if step == "A":
            return True
        if step == "R":
            return False
        if ":" not in step:
            return run_process(item, processes[step])
        c, r = step.split(":")
        if "<" in c:
            if item[c[0]] < int("".join([a for a in c if a.isnumeric()])):
                return run_process(item, processes[r])
            continue
        if ">" in c:
            if item[c[0]] > int("".join([a for a in c if a.isnumeric()])):
                return run_process(item, processes[r])
            continue
        print("PANIC!!!")

total = 0
for thing in parts:
    if run_process(thing, processes["in"]):
        total += sum(thing.values())

# Part two!
# reduce workflows?


print(total)
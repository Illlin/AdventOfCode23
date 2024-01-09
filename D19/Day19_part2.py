import json
processes = {"A": "A", "R": "R"}
for line in open("input"):
    if line == "\n":
        continue
    if "=" not in line:
        a, b = line.strip().split("{")
        processes[a] = b[:-1]


def calculate_possibilities(part):
    total = 1
    for i in part:
        total *= part[i][1] - part[i][0] + 1
    return total

total = 0

def run_process(item, process):
    global total
    for step in process.split(","):
        if step == "A":
            total += calculate_possibilities(item)
            return
            # Some logic to calculate how many
        if step == "R":
            return
        if ":" not in step:
            run_process(item, processes[step])
            return
        c, r = step.split(":")
        if "<" in c:
            # Split on thing
            var, num = c.split("<")
            num = int(num)
            if item[var][0] < num and item[var][1] < num:
                run_process(item, processes[r])
                return
            elif item[var][0] < num <= item[var][1]:
                it = json.loads(json.dumps(item))
                it[var][1] = num-1
                item[var][0] = num
                run_process(it, processes[r])
            elif item[var][0] >= num:
                pass
            else:
                pass
        if ">" in c:
            # Split on thing
            var, num = c.split(">")
            num = int(num)
            if item[var][0] > num and item[var][1] > num:
                run_process(item, processes[r])
                return
            elif item[var][1] > num >= item[var][0]:
                it = json.loads(json.dumps(item))
                it[var][0] = num+1
                item[var][1] = num
                run_process(it, processes[r])
            elif item[var][1] <= num:
                pass
            else:
                pass

run_process({"x":[1,4000],"m":[1,4000],"a":[1,4000],"s":[1,4000]}, processes["in"])

print(total)
pass
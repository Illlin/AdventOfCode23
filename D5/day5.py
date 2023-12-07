import numpy as np

def part_one():
    f = list(open("input"))
    f.append("\n")
    seeds = [int(a) for a in f[0].split()[1:]]
    alm = []
    for line in f[3:]:
        if "to" in line:
            continue
        if len(line) < 2:
            if len(alm) == 0:
                continue
            # Parse map
            for i, c in enumerate(seeds):
                for con in alm:
                    if c in con[0]:
                        seeds[i] = c+con[1]
            alm = []
        else:
            d, s, r = (int(i)for i in line.split())
            alm.append([range(s, s+r),d-s])
    print(min(seeds))


def part_two():
    f = list(open("input"))
    f.append("\n")
    raw_seed_ranges = np.array([int(a) for a in f[0].split()[1:]]).reshape(-1,2)
    seed_ranges = []
    for a in raw_seed_ranges:
        seed_ranges.append([a[0], a[0]+a[1]-1])

    alm = []
    for line in f[3:]:
        if "to" in line:
            continue
        if len(line) < 2:
            if len(alm) == 0:
                continue
            # Parse map
            output = []
            while len(seed_ranges) > 0:
                c = seed_ranges.pop()
                found = False
                for i in alm:
                    # condition not in range
                    #if c[1] < i[0] or c[0] > i[1]:
                    #    continue
                    # All in range
                    if i[0] <= c[0] <= i[1] and i[0] <= c[1] <= i[1]:
                        output.append([c[0]+i[2],c[1]+i[2]])
                        found = True
                        #break
                    # Split left
                    elif c[0] < i[0] < c[1]:
                        seed_ranges.append([c[0],i[0]-1])
                        seed_ranges.append([i[0],c[1]])
                        found = True
                        break
                    # Split right
                    elif c[0] < i[1] < c[1]:
                        seed_ranges.append([c[0], i[1]])
                        seed_ranges.append([i[1]+1, c[1]])
                        found = True
                        break
                if not found:
                    output.append(c)
            alm = []
            seed_ranges = output
            print(len(seed_ranges))
        else:
            d, s, r = (int(i)for i in line.split())
            alm.append([s, s+r-1,d-s])
    print(min([i[0] for i in seed_ranges]))


part_one()
part_two()

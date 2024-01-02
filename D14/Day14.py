import numpy as np

def part_one():
    a = np.array([[*x.strip()] for x in open("input")])

    # Spin North
    for _ in range(len(a)):
        for i in range(len(a)-1):
            fall = (a[i] == ".") & (a[i+1] == "O")
            a[i] = np.where(fall, "O", a[i])
            a[i+1] = np.where(fall, ".", a[i+1])

    total = 0
    for i in range(len(a)):
        total += sum(a[i] == "O") * (len(a)-i)

    print(total)


def cache_result(func):
    cache = {}

    def wrapper(a, c):
        key = a.tobytes()
        if key in cache:
            print("Itter", c, "is also itter ", cache[key][0])
            loop = c - cache[key][0]
            goal = (1000000000-cache[key][0])%loop + cache[key][0] - 1
            print([x for x in cache.values() if x[0]==goal-1])
            return cache[key]

        result = func(a, c)

        total = 0
        for i in range(len(a)):
            total += sum(result[i] == "O") * (len(result)-i)
        print(c, total)

        cache[key] = [c, total]

        return result

    return wrapper


@cache_result
def spin(a, _):
    for i in range(4):
        for _ in range(len(a)):
            for i in range(len(a) - 1):
                fall = (a[i] == ".") & (a[i + 1] == "O")
                a[i] = np.where(fall, "O", a[i])
                a[i + 1] = np.where(fall, ".", a[i + 1])
        a = np.rot90(a, k=3)
    return a

def part_two():
    a = np.array([[*x.strip()] for x in open("test")])
    for c in range(180):
        a = spin(a, c)

    total = 0
    for i in range(len(a)):
        total += sum(a[i] == "O") * (len(a)-i)
    print(c, total)
    pass

part_one()
part_two()
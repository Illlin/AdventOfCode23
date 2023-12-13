import re
from functools import cache

@cache
def count(pools, pat):
    if re.fullmatch(pat,pools):
        if "?" not in pools:
            return 1
        return count(pools.replace("?",".",1),pat)+count(pools.replace("?","#",1),pat)
    return 0

@cache
def count2(pools, P):
    if P == ():
        return 0 if "#" in pools else 1
    p = P[0]
    r = 0
    for i in range(len(pools)-len(P)-sum(P[1:])-p+2):
        if i+p < len(pools) and pools[i+p] == "#":
            continue
        if "#" in pools[:i]:
            break
        if "." not in pools[i:i+p]:
            r += count2(pools[i+p+1:],P[1:])
    return r

print(sum([(count(po,"^[?.]*"+"[?.]+".join([f"[?#]{{{i}}}" for i in [int(x) for x in pa.split(",")]])+"[?.]*")) for po,pa in [line.split() for line in open("test")]]))
#print(sum([(count("?".join([po]*5),[int(x) for x in pa.split(",")]*5)) for po,pa in [line.split() for line in open("test")]]))
print([sum(count2("?".join([po]*n), tuple([int(x) for x in pa.split(",")])*n) for po,pa in [line.split() for line in open("i")]) for n in (1,5)])

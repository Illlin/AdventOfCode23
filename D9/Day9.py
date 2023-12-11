import itertools as I
i = [[int(x) for x in y.split()] for y in open("input")]
def eat(a,d,s):
    if sum([abs(x) for x in a])>0:
        return a[d] + eat([c-b for b,c in I.pairwise(a)],d,s)*s
    return 0
print(sum([eat(x,-1,1) for x in i]))
print(sum([eat(x,0,-1) for x in i]))
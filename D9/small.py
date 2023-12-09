import itertools as I
i=[[*map(int,x.split())]for x in open(0)]
e=lambda a,d,s:any(a)and a[d]+e([c-b for(b,c)in I.pairwise(a)],d,s)*s
print([sum([e(x,*a)for x in i])for a in[(-1,1),(0,-1)]])
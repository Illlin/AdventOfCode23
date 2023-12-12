import itertools as I
a=[[b=='.'for b in a.strip()]for a in[*open("i")]]
def s(z):
 r,c=[[1+z*all(b)for b in c]for c in[a,zip(*a)]]
 f=[i for l in a for i in l]
 w=len(a[0]);i=[x for x in range(len(f))if not f[x]]
 print(sum([sum(c[x%w+1:y%w+1]+c[y%w+1:x%w+1]+r[x//w+1:y//w+1]+r[y//w+1:x//w+1])for(x,y)in I.combinations(i,2)]))
s(1)
s(999999)
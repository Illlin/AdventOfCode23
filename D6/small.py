from numpy import*
r,z,a=arange,lambda t,d:sum(r(t)*(t-r(t))>d),[a.split()[1:]for a in open(0)]
print(prod([z(int(a[0][i]),int(a[1][i]))for i in r(4)]),z(*[int(''.join(x))for x in a]))
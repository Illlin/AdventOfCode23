from functools import cache
H='#'
@cache
def C(d,P):
	if P==():return 0 if H in d else 1
	p=P[0];r=0
	for i in range(len(d)-len(P)-sum(P[1:])-p+2):
		if i+p<len(d)and d[i+p]==H:continue
		if H in d[:i]:break
		if'.'not in d[i:i+p]:r+=C(d[i+p+1:],P[1:])
	return r
print([sum(C('?'.join([d]*n),tuple([int(x)for x in p.split(',')])*n)for(d,p)in[l.split()for l in open('i')])for n in(1,5)])
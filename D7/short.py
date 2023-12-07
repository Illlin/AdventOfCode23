from numpy import*;u="0"
def a(s):
	o=[]
	for l in open(s):
		h,b=l.split()
		for a in['Kk','Ax','TC','J'+s]:h=h.replace(*a)
		j=h.count(u)*(s==u);_,c=unique([*h.replace(u,"")],0,0,1);c.sort()
		if j!=5:z=c[-1]+j
		if j==5or z==5:p='9'
		elif z==4:p='8'
		elif z==3and c[-2]==2:p='7'
		elif z==3:p='6'
		elif z==2and c[-2]==2:p='5'
		elif z==2:p='4'
		else:p=u
		o+=[[p+h,b]]
	o.sort(key=lambda x:x[0]);print(sum([int(c[1])*(i+1)for(i,c)in enumerate(o)]))
a('J');a('0')
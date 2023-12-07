import re
P=print
E=enumerate
P(sum(int(a[0]+a[-1])for a in(re.sub("\D","",i)for i in open("a"))))
N=["one","two","three","four","five","six","seven","eight","nine"]
t=0
for l in open("a"):
	m=""
	for i,c in E(l):
		for j,n in E(N):
			if l[i:i+len(n)]==n:m+=str(j+1)
		if c.isdigit():m+=c
	t+=int(m[0]+m[-1])
P(t)
import re,numpy as A
F=list(open('i'))
B={}
for H in F[2:]:I,J,K=re.sub('[()=,]','',H).split();B[I]=[K,J]
L=[A for A in B if A[-1]=='A']
C=[]
G=F[0].strip()
for D in L:
	E=0
	while D[-1]!='Z':D=B[D][G[E%len(G)]=="L"];E+=1
	C+=[E]
print(C[0],A.lcm.reduce(A.array(C)))
H='\\D'
G='input'
F='blue'
E='green'
D='red'
C=print
import re,numpy as J
def A():
	A=0;B={D:12,E:13,F:14}
	with open(G)as L:
		for(M,N)in enumerate(L):
			I=True
			for O in N.split(':')[1].split(';'):
				for J in O.split(','):
					P=int(re.sub(H,'',J))
					for K in B:
						if K in J:
							if P>B[K]:I=False
			if I:A+=M+1
	C(A)
def B():
	with open(G)as K:
		I=0
		for L in K:
			A={D:0,E:0,F:0}
			for M in L[:-1].split(':')[1].split(';'):
				for B in M.split(','):N=int(re.sub(H,'',B));A[B.split(' ')[-1]]=max(N,A[B.split(' ')[-1]])
			I+=J.prod(list(A.values()))
		C(I)
A()
B()
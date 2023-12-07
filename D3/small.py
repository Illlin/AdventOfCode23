L=print
J=tuple
I=set
G=int
F=len
E=enumerate
D=list
B=''
import numpy as A
def C():
	M='1234567890.';N=A.array([(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]);J=0
	with open('input')as O:
		H=A.array([D(A.strip('\n'))for A in D(O)])
		for(P,Q)in E(H):
			I=[];C=B
			for(R,K)in E(Q):
				if K.isdigit():C+=K;I+=[H[B,A]for(A,B)in N+[R,P]if 0<=A<F(H[0])and 0<=B<F(H)]
				else:
					if C!=B and A.array([A not in M for A in I]).any():J+=G(C)
					C=B;I=[]
			if C!=B and A.array([A not in M for A in I]).any():J+=G(C)
	L(J)
def H():
	Q=A.array([(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)])
	with open('test')as R:M=A.array([D(A.strip('\n'))for A in D(R)])
	K=[]
	for(S,T)in E(M):
		C=B;H=[]
		for(U,N)in E(T):
			if N.isdigit():H.append([S,U]);C+=N
			elif C!=B:K.append([G(C),I([J(A)for A in H])]);H=[];C=B
		if C!=B:K.append([G(C),I([J(A)for A in H])])
	O=0
	for V in A.array(A.where(M=='*')).T:W=I([J(A)for A in Q+V]);P=[A[0]for A in K if F(W.intersection(A[1]))>0];O+=A.prod(P)*(F(P)==2)
	L(O)
C()
H()
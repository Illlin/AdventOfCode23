def part_one():
    total = 0
    for line in list(open("input")):
        w,m=[x.lstrip().split(" ")for x in line.strip("\n").split(":")[1].replace("  "," ").split("|")]
        total += 2**(len(set(w)&(set(m)))-1) * (len(set(w)&(set(m))) > 0)
    print(total)


print(sum([2**(len(set(w)&(set(m)))-1)*(len(set(w)&(set(m)))>0)for w,m in[[y.strip().split(" ")for y in x]for x in[line.strip("\n").split(":")[1].replace("  "," ").split("|")for line in open("input")]]]))
print(sum([2**(len(set(w)&(set(m)))-1)*(len(set(w)&(set(m)))>0)for w,m in[[y.split()for y in x]for x in[l.strip("\n").split(":")[1].split("|")for l in open("input")]]]))
print(sum([2**(a-1)*(a>0)for a in[len(set(w)&(set(m)))for w,m in[[y.split()for y in x]for x in[l.strip("\n").split(":")[1].split("|")for l in open("i")]]]]))

print("Smallest")
print(sum([2**(A-1)*(A>0)for A in[len(set(A)&set(B))for(A,B)in[[A.split()for A in A]for A in[A.strip('\n').split(':')[1].split('|')for A in open('i')]]]]))
C=len
A={}
for(B,D)in enumerate(list(open('input'))):E,F=[set(A.lstrip().split())for A in D.split(':')[1].split('|')];A[B]=list(range(B+1,B+C(E&F)+1))
for B in A:A[C(A)-B-1]=[A[B]for B in A[C(A)-B-1]]
print(str(A).count('['))


s=str.split;print(sum([2**a*(a>=0)for a in[len(set(w)&set(m))-1 for w,m in[[s(y)for y in x]for x in[s(s(l,":")[1],"|")for l in open("i")]]]]))

import re;print(sum([2**a*(a>=0)for a in[len(set(w)&set(m))-1 for w,m in[(a[1:11],a[11:])for a in[re.sub("[^0-9 ]","",l).split()for l in open("i")]]]]))


def part_two():
    total = 0
    mapping = {}
    with open("input") as f:
        for i, line in enumerate(list(open("input"))):
            w, m = [set(x.lstrip().split()) for x in line.split(":")[1].split("|")]
            mapping[i] = list(range(i + 1, i + len(w & m) + 1))
    inbox = list(mapping.keys())
    while len(inbox) > 0:
        total += 1
        current = inbox.pop()
        inbox += mapping[current]
    print(total)


def part_two_r():
    mapping = {}
    for i, line in enumerate(list(open("input"))):
        w,m = [set(x.lstrip().split()) for x in line.split(":")[1].split("|")]
        mapping[i] = list(range(i+1, i+len(w & m)+1))
    for i in mapping:
        mapping[len(mapping)-i-1] = [mapping[j] for j in mapping[len(mapping)-i-1]]
    print(str(mapping).count("["))

# Part 2 Mini
C=len
A={}
for(B,D)in enumerate(list(open('input'))):E,F=[set(A.lstrip().split())for A in D.split(':')[1].split('|')];A[B]=list(range(B+1,B+C(E&F)+1))
for B in A:A[C(A)-B-1]=[A[B]for B in A[C(A)-B-1]]
print(str(A).count('['))


part_one()
part_two_r()
part_two()

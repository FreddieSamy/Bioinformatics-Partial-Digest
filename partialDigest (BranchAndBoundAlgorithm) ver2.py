def delta(y,x):
    res=list()
    for i in x:
        res.append(abs(y-i))
    return res
def branching(L,x):
    if len(L)==0:
        x.sort()
        print(x)
        return
    y=max(L)
    place(y,x,L)
    place(max(x)-y,x,L)
def place(y,x,L):
    tL=L.copy()
    tx=x.copy()
    deltaYX=delta(y,x)
    if all(z in tL for z in deltaYX):
        tx.append(y)
        [tL.remove(z) for z in deltaYX]
        branching(tL,tx)
L=input("Enter L numbers separated by , :")
L=L.split(',')
for i in range(len(L)):
    L[i]=int(L[i])
L.sort()
length=L.pop()
x=[0,length]
branching(L,x)

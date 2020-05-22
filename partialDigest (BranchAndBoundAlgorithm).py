def delta(y,x):
    res=list()
    for i in x:
        res.append(abs(y-i))
    return res
def place(L,x):
    if len(L)==0:
        x.sort()
        print(x)
        return
    y=max(L)
    deltaYX=delta(y,x)
    if all(z in L for z in deltaYX):
        x.append(y)
        [L.remove(z) for z in deltaYX]
        place(L,x)
        x.remove(y)
        L.extend(deltaYX)
    deltaYX=delta(max(x)-y,x)
    if all(z in L for z in deltaYX):
        x.append(max(x)-y)
        [L.remove(z) for z in deltaYX]
        place(L,x)
        x.remove(max(x)-y)
        L.extend(deltaYX)
L=input("Enter L numbers separated by , :")
L=L.split(',')
for i in range(len(L)):
    L[i]=int(L[i])
L.sort()
length=L.pop()
x=[0,length]
place(L,x)

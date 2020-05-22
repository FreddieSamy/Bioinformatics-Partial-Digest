x=input("Enter L numbers separated by , :")
x=x.split(',')
for i in range(len(x)):
    x[i]=int(x[i])
x.sort()
L=tuple(x)
import math
n=int(0.5+(0.5*math.sqrt(1+(8*len(L)))))
Max=x.pop()
x=list(dict.fromkeys(x))
import itertools
print("possible solutions:")
for x in list(itertools.combinations(x,n-2)):
    x=list(x)
    x.insert(0,0)
    x.append(Max)
    delta_x=list()
    for i in range(len(x)-1,0,-1):
        for j in range(i-1,-1,-1):
            delta_x.append(x[i]-x[j])
    delta_x.sort()
    if tuple(delta_x) == L:
        print(x)

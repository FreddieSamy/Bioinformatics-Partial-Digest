short=input("Enter short experiment numbers separated by , :")
short=short.split(',')
for i in range(len(short)):
    short[i]=int(short[i])
short.sort()
long=input("Enter long experiment numbers separated by , :")
long=long.split(',')
for i in range(len(long)):
    long[i]=int(long[i])
long.sort()
length=sum(long)


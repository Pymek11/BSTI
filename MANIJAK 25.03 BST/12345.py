e=31
n=3599
M=10
C=M**e%n
d=1
while(True):
    if(C**d%n==M):
        print(d)
        break
    else:
        d += 1
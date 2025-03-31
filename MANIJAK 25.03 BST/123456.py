q=71
a=7

y=3
k=2
M=30


C1=(a**k)%q
C2=((y**k)*M)%q

print(C1,C2)

M=30
C1=59
K=0
while(True):
    if((a**K)%q==C1):
        print(K)
        break
    else:
        K+=1
C2=((y**K)*M)%q
print(C2)
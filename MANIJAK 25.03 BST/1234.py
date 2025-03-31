C=30
e=11
n=65
M=0
x=0
while(M==0):
    x+=1
    if((x**e)%n==C):
        M=x

print(M)
print((M**e)%n==C)
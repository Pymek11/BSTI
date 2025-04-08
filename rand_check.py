import random
import math

nums=0
all_pairs=0
for i in range(10000):
    num1=random.randint(1,1000)
    num2=random.randint(1,1000)
    if math.gcd(num1,num2)==1:
        nums+=1


all_pairs += i+1
percentage=nums/all_pairs
print(percentage)

pi=math.sqrt(6/percentage)  #ernesto cesaro theorem
print(pi)
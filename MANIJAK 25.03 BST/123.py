p=7
q=23
x = (p-1)*(q-1)
#print(x)
e =13 #  x<132
n=p*q
#print(n)
#klucz publiczny (e,n)->(13,161)

#(d*e)mod(x)==1
d=0
y=0
while(d==0):
    y+=1
    if((y*e)%x==1):
        d=y

print(d) # klucz prywatny

print(61*e%x)  #sprawdzenie

# e=13 n=161 d=61

#szyfrowanie
M=15
print("Liczba wyslana: ", M)# wiadomosc

C= (M**e) %n
print("Zaszyfrowana liczba: ",C)
#deszyfrowanie
M=(C**d)%n
print("Deszyfrowana liczba: " ,M)

#liczba musi byc mniejsza od liczby n ,w moim przypadku mniejsza od 161
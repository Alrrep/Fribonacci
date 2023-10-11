#!/usr/bin/env python3

#GNU/GLP License
#My first secuence
#sumar los 10 primeros 
#suma= 1+2+3+4+5+6+7+8+9+10
#print(suma)
import math
fibo=[]
N=100
a=1
b=1
#print(a)
#print(b)
fibo.append(a)
fibo.append(b)
for x in range(N+1):
    c=a+b
    #print(c)
    fibo.append(c)
    a=b
    b=c
print(fibo)

for i in range(len(fibo)-1):
    print(fibo[i+1]/fibo[i])

gold_ration=fibo[-1]/fibo[-2]
print(gold_ration)

#Razon dorada
#print((1.0+math.sqrt(5))/2.0)

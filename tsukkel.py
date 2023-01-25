from math import *
from random import*

#try:
#    a=int(input("Mitu päevad nädalas ->"))
#    while True:
#        if a!=7:
#            print("Veidi üle poole")
#            a=int(input("Mitu päevad nädalas ->"))
#        else:
#            print("Õige vastus")
#            break
#except:
#    print("Vale andmed")





#try:
#    a=int(input("Mitu päevad nädalas ->"))
#    while a<7:
#        if a==7:
#            print("Õige vastus")
#        else:
#            a=int(input("Mitu päevad nädalas ->"))
#except:
#    print("Vale andmed")



#n=int(input("Mitu toa korteris? ->"))
#for i in range(1,n+1,1): 
#    t=float(input(f"{i}. toa Temperatuur: "))
#    if t>18: 
#        print("Soe")
#    else: 
#        print("Külm")


N = random.randint(1, 10)
M = random.randint(1, 10)
print("numbrid on:")
for i in range(1, N+1):
    print(i**2, end =" ")
for j in range(1, M+1):
    print(j**3, end =" ")






x=1
while True:
    if x>100:
        break
    elif x%5==0:
        print(x, end=" ")
    x+=1


  



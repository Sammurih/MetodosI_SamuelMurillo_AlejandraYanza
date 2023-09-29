import numpy as np
import sympy as sym
import math
R=0.5
a=0.01
n=100000
x = np.linspace(-a,a,n)
IntegralTeorica=np.pi*(R-np.sqrt(R**2-a**2))

#print(x)

def Function(x):
    a=0.01
    R=0.5
    return (np.sqrt(a**2-x**2))/(R+x)

y = Function(x)

def IntegrateTrapecio(n,x,y):
    h=x[1]-x[0]
    sum=0
    for i in range(0,n):
        if i==0:
            sum+=y[i]
        elif i==n-1:
            sum+=y[i]
        else:
            sum+=2*y[i]
    return (h/2)*sum

def Error(Teorico,Experimental):
    return 100*(1-np.abs(Experimental)/np.abs(Teorico))
IntegralTrapecio=IntegrateTrapecio(n,x,y)

print(IntegralTeorica) 

print(IntegralTrapecio)
print(Error(IntegralTeorica,IntegralTrapecio))

def Simpson(x,y):
    h=(x[1]-x[0])/2
    x1=x[0]
    suma=0
    for i in range(1,len(x)):
        x2=x[i]
        xm=(x2+x1)/2
        suma+=(h/3)*(y(x1)+4*y(xm)+y(x2))
        x1=x2
    return suma

IntegralSimpson=Simpson(x,Function)
print(IntegralSimpson)
print(Error(IntegralTeorica,IntegralSimpson))

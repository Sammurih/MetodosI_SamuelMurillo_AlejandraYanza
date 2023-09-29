import numpy as np
import sympy as sym 
from scipy import integrate


n=2
R, W = np.polynomial.laguerre.laggauss(n)


def GetLaguerreRecursive(n,x):
    if n==0:
        poly = sym.Number(1)
    elif n==1:
        poly = 1-x
    else:
        poly = ((2*n-1-x)*GetLaguerreRecursive(n-1,x)-(n-1)*GetLaguerreRecursive(n-2,x))/n
    return sym.expand(poly,x)

x = sym.Symbol('x',real=True)

L2=GetLaguerreRecursive(n,x)
print(L2)

Raices=sym.solve(L2)
print(Raices)
print(R)

x1=Raices[0]
x2=Raices[1]

w1=sym.integrate(sym.exp(-x)*(x-x2)/(x1-x2),(x,0,sym.oo))
w2=sym.integrate(sym.exp(-x)*(x-x1)/(x2-x1),(x,0,sym.oo))
print(w1)
print(w2)
print(W)

#Si x=a y t=x en Gamma, para grado 3, entonces a=4
a=4
Gamma=sym.integrate(sym.exp(-x)*x**(a-1),(x,0,sym.oo))

#Si gamma es (a-1)!, con a=4, Gamma=6

print(Gamma)

poly=sym.lambdify([x],x**3,"numpy")
sumatoria=w1*poly(Raices[0])+w2*poly(Raices[1])
sumatoria = sym.simplify(sumatoria)
print(sumatoria)
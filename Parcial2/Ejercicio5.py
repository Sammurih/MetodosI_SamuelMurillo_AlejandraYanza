from sympy import exp, diff, solve, factorial, symbols
x=symbols("x")
for i in range(21):
    L_i = exp(x) / factorial(i) * diff(exp(-x) * x**i, x, i)
    roots = solve(L_i, x, domain=(0, float('inf')))
    roots = [root.evalf() for root in roots] 
    print(f"LAS RACICES DEL POLINOMIO DE LAGUERRE L_{i}(x) son: ({', '.join(map(str, roots))})\n")

import numpy as np
import sympy as sym
import math

n=20

x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)

def GetLaguerre(n,x):
    y = (sym.exp(-x))*x**n
    poly = (sym.exp(x)*sym.diff( y,x,n ))/(math.factorial(n))
    return poly

Laguerre=GetLaguerre(n,x)
DLaguerre=sym.diff(Laguerre,x,1)

def GetNewton(f,df,xn,itmax=10000,precision=1e-10):
    error = 1.
    it = 0
    while error >= precision and it < itmax:
        try:
            xn1 = xn - f(xn)/df(xn)
            error = np.abs(f(xn)/df(xn))
        except ZeroDivisionError:
            print('Zero Division')
        xn = xn1
        it += 1
    if it == itmax:
        return xn
    else:
        return xn
    
def GetRoots(f,df,x,tolerancia = 5):
    Roots = np.array([])
    for i in x:
        if len(Roots) < 20:
            root = GetNewton(f,df,i)
            if root != False:
                croot = np.round( root, tolerancia )
                if croot not in Roots:
                    Roots = np.append(Roots, croot)
    Roots.sort()
    return Roots

def GetAllRootsLaguerre(n,xn,Laguerre,DLaguerre):
    poly = sym.lambdify([x],Laguerre,'numpy')
    Dpoly = sym.lambdify([x],DLaguerre,'numpy')
    Roots = GetRoots(poly,Dpoly,xn)
    return Roots

def GetWeightsLaguerre(n,xn,Laguerre,DLaguerre):
    Roots = GetAllRootsLaguerre(n,xn,Laguerre,DLaguerre)
    poly = sym.lambdify([x],GetLaguerre(n+1,x),'numpy')
    Weights = Roots/(((n+1)**2)*(poly(Roots))**2)
    return Weights

xn=np.exp(np.linspace(0,np.log(n+(n-1)*np.sqrt(n)),70))
#print(xn)

print(Laguerre)

RootsLaguerre=GetAllRootsLaguerre(n,xn,Laguerre,DLaguerre)

print(RootsLaguerre)

WeightsLaguerre=GetWeightsLaguerre(n,xn,Laguerre,DLaguerre)

print(WeightsLaguerre)

#print(np.polynomial.laguerre.laggauss(n))
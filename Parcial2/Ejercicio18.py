import numpy as np
import sympy as sym
import math

n=20

x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)

def GetNewton(f,df,xn,itmax=20000,precision=1e-13):
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
    
def GetRoots(f,df,x,tolerancia = 10):
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

def GetHermite(n,x):
    y = (sym.exp(-x**2))
    poly = (-1**n*sym.exp(x**2)*sym.diff( y,x,n ))
    return poly

def GetDHermite(n,x):
    Pn = GetHermite(n,x)
    return sym.diff(Pn,x,1)

def GetAllRootsGHer(n):
    
    xn = np.linspace(-1*np.sqrt(4*n+1),np.sqrt(4*n+1),100)
    
    poly = sym.lambdify([x],GetHermite(n,x),'numpy')
    Dpoly = sym.lambdify([x],GetDHermite(n,x),'numpy')
    Roots = GetRoots(poly,Dpoly,xn)
    
    if len(Roots) != n:
        ValueError('El número de raíces debe ser igual al n del polinomio.')

    return Roots

def GetWeightsGHer(n):

    Roots = GetAllRootsGHer(n)
    
    poly = sym.lambdify([x],GetHermite(n-1,x),'numpy')
    Weights = ((2**(n-1))*math.factorial(n)*np.sqrt(np.pi))/((n**2)*(poly(Roots))**2)
    
    return Weights

Hermite=GetHermite(n,x)
print(Hermite)

RootsHermite=GetAllRootsGHer(n)
print(RootsHermite)

WeightsHermite=GetWeightsGHer(n)
print(WeightsHermite)



def oscilador (x):
    return np.sqrt(1/np.pi) *2*x**4

h=0
for i in range(7):
    h+=GetWeightsGHer(8)[i]*oscilador(GetAllRootsGHer(8)[i])
print(h)





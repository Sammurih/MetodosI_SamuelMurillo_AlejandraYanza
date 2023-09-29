import numpy as np
import sympy as sym 
from scipy import integrate

def GetLaguerre(n,x):

    if n==0:
        poly = sym.Number(1)
    elif n==1:
        poly = 1-x
    else:
        poly = ((2*n-1-x)*GetLaguerre(n-1,x)-(n-1)*GetLaguerre(n-2,x))/n
   
    return sym.expand(poly,x)

x = sym.Symbol('x',real=True)
L2=GetLaguerre(2,x)
print(L2)
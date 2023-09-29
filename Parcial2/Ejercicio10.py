import numpy as np
import sympy as sym 
from scipy import integrate

x = sym.Symbol('x',real=True)
h = sym.Symbol('h',real=True)
f = sym.Symbol('f^4(E)',real=True)
E=sym.integrate(x*(x-h)*(x-2*h)*(x-3*h),(x,0,3*h))
print(f*E/24)
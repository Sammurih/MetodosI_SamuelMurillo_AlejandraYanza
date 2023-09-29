import numpy as np
import sympy as sym
import math

a=0.01
R=0.5
f = lambda x: (np.sqrt(a**2+x**2))/(R+x)

x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)
n=6

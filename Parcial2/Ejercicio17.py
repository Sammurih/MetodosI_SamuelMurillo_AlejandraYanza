import numpy as np
import sympy as sym
from scipy import integrate

def gauss_integrate(n):
  f = lambda x: x**3 / (np.exp(x)-1)
  Roots1, Weights1 = np.polynomial.laguerre.laggauss(n)
  X = np.array(Roots1)
  W = np.array(Weights1)
  suma = 0 

  for i in range(len(X)):
      suma += W[i]* f(X[i])
      
  gauss_int = suma
  

  return gauss_int

print(gauss_integrate(3))
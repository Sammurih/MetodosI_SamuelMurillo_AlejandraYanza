import numpy as np
import sympy as sym 
from scipy import integrate


h=6.626*1e-34
k=1.3806*1e-23
c=3*1e8
T=5772
lambda0=100*1e-9
lambda1=400*1e-9
n=20


#Para el numerador podemos hacer una cuadratura de Gauss-Legendre con limites de a a b
def FuncionNumerador(x):
    return x**3/(np.exp(x)-1)
R1, W1 = np.polynomial.legendre.leggauss(n)
#Para los límites de Integración
v0=c/lambda0
v1=c/lambda1
b=(h*v0)/(k*T)
a=(h*v1)/(k*T)

t = 0.5*( (b-a)*R1 + a + b )
IntegralNumerador = 0.5*(b-a)*np.sum(W1*FuncionNumerador(t))
#print(IntegralNumerador)
print(b-a)

#Para el denominador podemos reescribir la función y hacemos una cuadratura de Gauss-Laguerre

def FuncionDenominador(x):
    return x**3/(1-1/(np.exp(x)))

R2, W2 = np.polynomial.laguerre.laggauss(n)

IntegralDenominador=np.sum(W2*FuncionDenominador(R2))
#print(IntegralDenominador)

F=IntegralNumerador/IntegralDenominador
print(F)

print("El porcentaje de rayos UV que llegan a la Tierra es de: "+str(round(100*F,1))+"%.")

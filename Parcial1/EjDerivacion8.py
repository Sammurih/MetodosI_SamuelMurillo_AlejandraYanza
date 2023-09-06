#Derivación: 8
import numpy as np
import matplotlib.pyplot as plt

def Function (x):
    return np.sqrt(np.tan(x))

X=np.linspace(0.1,1.1,100)
Y=np.zeros(len(X))
h=0.01
for i in range(0,len(X)):
    Y[i]=Function(X[i])

plt.plot(X,Y,label="Función")

def derivada_progresiva_h_cuadrado (X,f,h):
    DpY=np.zeros(len(X))
    for i in range(0,len(X)):
        DpY[i]=(-3*f(X[i])+4*f(X[i]+h)-f(X[i]+2*h))/(2*h)
    return DpY

DpY= derivada_progresiva_h_cuadrado (X,Function,h)

plt.plot(X,DpY,label="Derivada Progresiva")

def derivada_central_h_cuadrado (X,f,h):
    DcY=np.zeros(len(X))
    for i in range (0,len(X)):
        DcY[i]=(f(X[i]+h)-f(X[i]-h))/(2*h)
    return DcY

DcY= derivada_central_h_cuadrado (X,Function,h)

plt.plot(X,DcY,label="Derivada Progresiva")
plt.legend()
plt.show()
#Derivación: 8
import numpy as np
import matplotlib.pyplot as plt

def Function (x):
    return np.sqrt(np.tan(x))
def Derivada_Teorica(x):
    return 0.5/((np.sqrt(np.tan(x)))*(np.cos(x))**2)
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

def Calcular_Error (X,dT,d2):
    ErrY=np.zeros(len(X))
    for i in range (0,len(X)):
        #print(dT(X[0]))
        ErrY[i]=np.abs(dT(X[i])-d2[i])
    return ErrY
#print(Derivada_Teorica(0.1))
ErrProgresivaY=Calcular_Error(X,Derivada_Teorica,DpY)
ErrCentralY=Calcular_Error(X,Derivada_Teorica,DcY)
plt.plot(X,ErrProgresivaY,label="Error Der. Progresiva")
plt.plot(X,ErrCentralY,label="Error Der. Central")
plt.legend()
plt.show()
#La Derivada Central tiene un menor error nodal, luego, esta es una mejor aproximación porque es más precisa que la proguresiva
#Interpolación de Lagrange: 4
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sym

import os
import os.path as path
import wget

if not path.exists('DataP3'):
    os.mkdir('DataP3')
    
file = 'DataP3/Parabolico.dat'
url = 'https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/Parabolico.csv'

if not path.exists(file):
    Path_ = wget.download(url,file)
    print('Archivo descargado')
else:
    print('---Archivo encontrado---')
    Path_ = file

Data = pd.read_csv(Path_,sep=',')
print(Data)

X=np.array(Data.X)
Y=np.array(Data.Y)
plt.scatter(X,Y,s=10)
plt.show()

def InterpolacionNewtonGregory(X,Y,x):
    sum_ = Y[0]
    Diff = np.zeros(( X.shape[0],Y.shape[0] ))
    h = X[1]-X[0]
    Diff[:,0] = Y
    poly = 1.
    
    for i in range(1,len(X)):
        poly *= (x-X[i-1])
        for j in range(i,len(X)):
            Diff[j,i] = Diff[j,i-1] - Diff[j-1,i-1] 
        sum_ += poly*Diff[i,i]/(np.math.factorial(i)*h**(i))
        
    return sum_

xt = np.linspace(np.min(X),np.max(X),50)
yt = []

for x in xt:
    yt.append(InterpolacionNewtonGregory(X,Y,x))
 
plt.scatter(X,Y,color='r')
plt.plot(xt,yt)
plt.show()

x = sym.Symbol('x',real=True)
y = InterpolacionNewtonGregory(X,Y,x)
y = sym.simplify(y)

g=-9.8
c=round(float(str(y).split("+")[2]),8)
b=round(float(str(y).split("+")[1].split("*")[0]),8)
a=round(float(str(y).split("+")[0].split("*")[0]),8)
print(a,b,c)

theta=round(np.arctan(b)*180/(np.pi),5)
v0=round(np.sqrt(g/(2*a*(np.cos((theta*np.pi)/180))**2)),5)
print("La velocidad inicial es: "+str(v0)+"m/s, y El ángulo de lanzamiento es: "+str(theta)+"°.")
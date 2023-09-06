import numpy as np
import matplotlib.pyplot as plt

def Function(X):
    return ((np.e)**(-X))-X

def SoporteX(a,b,F):
    X=np.array([0.,0.,0.,])
    if F(a)*F(b) < 0:
        X[0]=a
        X[2]=b
        X[1]=(a+b)/2
        np.sort(X)
    else:
        print("No hay una raiz en el intervalo")
    return X

X=SoporteX(-3.5,5,Function)
Y=Function(X)
plt.scatter(X,Y,s=10)
plt.axhline(y = 0,color='r')
plt.show()

def EncontrarX3 (X,a,b,c):
    if b<0:
        x3=(-2*c)/(b-np.sqrt(b**2-4*a*c))
    else:
        x3=(-2*c)/(b+np.sqrt(b**2-4*a*c))
    return x3

def diferencia_div_2 (x0, x1, F):
    resul= (F(x1)-F(x0))/(x1-x0)
    return resul

def diferencia_div_3(x0,x1,x2,F):
    resul= (diferencia_div_2(x1,x2,F)- diferencia_div_2(x0,x1,F))/(x2-x0)
    return resul

def define_abc(x0,x1,x2,F):
    a=diferencia_div_3(x0,x1,x2,F)
    b=diferencia_div_2(x0,x1,F)-((x0+x1)*(diferencia_div_3(x0,x1,x2,F)))
    c=F(x0)-((x0)*diferencia_div_2(x0,x1,F))+(x0*x1*diferencia_div_3(x0,x1,x2,F))

    return np.array([a,b,c])

def hallar_x3(X,F):
    e=np.abs(F(X[2]))
    iter=0
    while e >= 1e-10 and iter < 100:
        a=define_abc(X[0],X[1],X[2],Function)[0]
        b=define_abc(X[0],X[1],X[2],Function)[1]
        c=define_abc(X[0],X[1],X[2],Function)[2]
        X[0]=X[1]
        X[1]=X[2]
        X[2]=EncontrarX3(X,a,b,c)
        e=np.abs(F(X[2]))
        iter+=1
    return X[2]

print("la raiz de la función es "+str(hallar_x3(X,Function)))
  


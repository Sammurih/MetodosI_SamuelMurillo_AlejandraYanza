import numpy as np
import matplotlib.pyplot as plt

def Function (x):
    return 3*(x)**5 +5*(x)**4 - (x)**3

x = np.linspace(-2,1,100)
y = Function(x)

plt.plot(x,y)
plt.axhline(y = 0,color='r')
plt.show()

def Derivative(f,x,h=1e-6):
    return (f(x+h)-f(x-h))/(2*h)

def GetNewtonMethod(f,df,xn,itmax=1000,precision=1e-8):
    error = 1.
    it = 0
    while error > precision and it < itmax:
        try:
            xn1 = xn - f(xn)/df(f,xn)
            error = np.abs(f(xn)/df(f,xn))
        except ZeroDivisionError:
            print('Division por cero')
            
        xn = xn1
        it += 1
    print('Raiz',xn,it)
    return xn

root = GetNewtonMethod(Function,Derivative,0)
print(root)

def GetAllRoots(x, tolerancia=6):
    Roots = np.array([])
    for i in x:
        root = GetNewtonMethod(Function,Derivative,i)
        if root != False:
            croot = np.round(root, tolerancia)
            if croot not in Roots:
                Roots = np.append(Roots,croot)
                
    Roots.sort()
    return Roots

Roots = GetAllRoots(x)
raices=""
for i in range(0,len(Roots)):
    if i==0:
        raices+=str(Roots[i])
    else:
        raices+=", "+str(Roots[i])
if raices=="":
    print("No hay raices")
else:
    print("Las raices son: " +raices)
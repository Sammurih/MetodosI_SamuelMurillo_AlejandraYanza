import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
x = np.linspace(-5,5,100)
y = np.zeros((3,len(x)))

y[0] = 2*x - 2.
y[1] = 0.5 - 0.5*x
y[2] = 4 - x

f1 =lambda _x,_y: 2*_x -_y - 2.
f2 =lambda _x,_y: _x + 2*_y - 1.
f3 =lambda _x,_y: _x +_y - 4.

A= np.array([[2,-1],
             [1,2],
             [1,1]])

b = np.array([2,1,4])

def GetMinimosCuadradosMatrizVector(A,b):

    AT = np.dot(A.T,A)
    bT = np.dot(A.T,b)

    xsol = np.linalg.solve(AT,bT)
    
    return xsol

print(GetMinimosCuadradosMatrizVector(A,b))
xsol=GetMinimosCuadradosMatrizVector(A,b)
for l in range(y.shape[0]):
    plt.plot(x,y[l],ls='--',lw=2)
plt.scatter(xsol[0],xsol[1],color='r')
plt.show()

# Esta sería la menor distancia
print(np.linalg.norm(np.dot(A,xsol)-b))

#AHORA HACIENDO UNA BUSQUEDA ITERATIVA

def IterativeMinimize(A,b,h=0.05):
    resultados=np.array([])
    puntos=np.array([[0,0]])
    x_= np.arange(-5,5,h)
    y_= np.arange(-5,5,h)
    for i in x_:
        for j in y_:
            resultados=np.append(resultados,np.linalg.norm(np.matmul(A,[i,j])-b))
            punto=(i,j)
            puntos=np.append(puntos,[punto],axis=0)
            print(resultados[-1])
            print(puntos[-1])
    resultados1=np.sort(resultados)
    #print(np.where(resultados==resultados1[0]))
    #print(np.where(resultados==resultados1[0])[0])
    return resultados1[0],puntos[np.where(resultados==resultados1[0])[0]+1]
D,P=IterativeMinimize(A,b)
print(D,P)


for l in range(y.shape[0]):
    plt.plot(x,y[l],ls='--',lw=2)
plt.scatter(xsol[0],xsol[1],color='r')
plt.scatter(P[0][0],P[0][1],color='b')
plt.show()

# Generar datos
x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)
x, y = np.meshgrid(x, y)
z = np.sqrt(f1(x,y)**2+f2(x,y)**2+f3(x,y)**2)

# Crear la figura y los ejes 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot 3D
ax.plot_surface(x, y, z, cmap='viridis')

# Configurar etiquetas
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# Mostrar el gráfico
plt.show()

#ITERATIVAMENTE ES MUCHO MÁS PESADO COMPUTACIONALMENTE Y NO ES TAN PRECISO COMO EL MÉTODO DE MÍNIMOS CUADRADOS
#MÍNIMOS CUADRADOS
#2.5354627641855494 [1.42857143 0.42857143]
#ITERATIVO
#2.5358233376952746 [[1.44 0.44]]
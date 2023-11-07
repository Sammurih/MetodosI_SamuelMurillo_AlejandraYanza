import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def Function(x,y):
    return x**2-y**2+2*x

x1,y1=1.,1.

Dx = lambda a1,a2,h=1e-5: (Function(a1+h,a2) - Function(a1-h,a2))/(2*h)
Dy = lambda a1,a2,h=1e-5: (Function(a1,a2+h) - Function(a1,a2-h))/(2*h)

x=np.linspace(-4,4,50)
y=np.linspace(-4,4,50)
x, y = np.meshgrid(x, y)
z = x**2 - y**2 + 2*x

#Plano tangente al punto (x1,y1,f(x1,y1))
Z=Function(x1,y1)+Dx(x1,y1)*(x-x1)+Dy(x1,y1)*(y-y1)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_zlim(-10, 10)
ax.plot_surface(x, y, z, cmap='coolwarm',alpha=0.5)
ax.plot_surface(x, y, Z, color='blue',alpha=0.3)
ax.scatter([1], [1], [2], color='red', s=10)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
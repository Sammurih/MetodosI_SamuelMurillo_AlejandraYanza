import numpy as np

N=int(1e5)
p=0
for i in range(N):
    Simulacion=np.random.choice([-1, 1], size=4)
    if np.sum(Simulacion) == 0:
        p+=1
p/=N
print(p) #Probabilidad de obtener dos caras (+2) y dos sellos (-2)
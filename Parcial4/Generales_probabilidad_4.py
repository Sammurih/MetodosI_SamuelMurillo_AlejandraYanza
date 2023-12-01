import matplotlib.pyplot as plt

def calcular_probabilidad_cumpleaños(n):
    probabilidad = 1.0
    for i in range(1, n+1):
        probabilidad *= (365-i+1)/365
    return probabilidad

x = range(1, 81)
y = [calcular_probabilidad_cumpleaños(n) for n in x]

plt.plot(x, y)
plt.xlabel('Número de personas (n)')
plt.ylabel('Probabilidad P(n ≤ 80)')
plt.title('Probabilidad de que n personas tengan fechas de cumpleaños diferentes')
plt.grid(True)
plt.show()
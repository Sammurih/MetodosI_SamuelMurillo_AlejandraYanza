import numpy as np
def band(x, Temp, difT):
    r = ((np.tanh((x**2 + difT**2)**(0.5) * 300/(2*Temp)))/(x**2 + difT**2)**(0.5))/2
    return r
def critic(R, W, T, d):
    for temp in T:
        integral = np.sum(W * band(R, temp, d))
        if np.isclose(integral, 1/0.3, rtol=1e-9, atol=d):
            return temp
R, W = np.polynomial.legendre.leggauss(100)
T, d = np.linspace(1, 20, 10000, retstep=True)
critical_temp = round(critic(R, W, T, d), 5)
print("La temperatura crítica es:", critical_temp, "K.")
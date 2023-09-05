from sympy import diff, solve, symbols

x=symbols("x")
f =3*(x)**5 +5*(x)**4 - (x)**3
der=diff(f,x,1)
raiz= solve(der,x)

print (raiz)


import pandas as pd



def leerarchivo(codigo):
    archivo = pd.read_csv(codigo, skiprows=[0], header=None, names=['x', 'y'])
    return archivo['x'].values, archivo['y'].values

def interpolacion_lagrange(x, datos_x, datos_y):
    x= 1.0
    n = len(xi)
    
    for j in range(n):
        num, den = 1.0, 1.0
        
        for i in range(n):
            if i != j:
                num *= (x - xi[i])
                den *= (xi[j] - xi[i])
        
        prod += yi[j] * (num / den)
    
    return prod
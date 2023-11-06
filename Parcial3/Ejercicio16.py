import numpy as np
import sympy as sp

I = sp.I
gamma0 = sp.Matrix([[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, -1, 0],
                   [0, 0, 0, -1]])
gamma1 = sp.Matrix([[0, 0, 0, 1],
                   [0, 0, 1, 0],
                   [0, -1, 0, 0],
                   [-1, 0, 0, 0]])
gamma2 = sp.Matrix([[0, 0, 0, -I],
                   [0, 0, I, 0],
                   [0, I, 0, 0],
                   [-I, 0, 0, 0]])
gamma3 = sp.Matrix([[0, 0, 1, 0],
                   [0, 0, 0, -1],
                   [-1, 0, 0, 0],
                   [0, 1, 0, 0]])


A = sp.MatrixSymbol('A', 4, 4)
B = sp.MatrixSymbol('B', 4, 4)

# Calcular el anticonmutador {A, B}
anticonmutador = sp.Mul(A, B) + sp.Mul(B, A)

# Sustituir las matrices de símbolos en el anticonmutador
anticonmutador = anticonmutador.subs({A: gamma0, B: gamma3})

sp.pprint(sp.expand(anticonmutador))
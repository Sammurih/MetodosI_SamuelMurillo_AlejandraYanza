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
Matrices=[gamma0,gamma1,gamma2,gamma3]

A = sp.MatrixSymbol('A', 4, 4)
B = sp.MatrixSymbol('B', 4, 4)
anticonmutador = sp.Mul(A, B) + sp.Mul(B, A)
for i in range(len(Matrices)):
    for j in range(len(Matrices)):
        print("gamma"+str(i),"gamma"+str(j))
        sp.pprint(sp.expand(anticonmutador.subs({A: Matrices[i], B: Matrices[j]})))

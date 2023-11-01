import numpy as np
from math import ceil
H = np.array([[1, 2, -1],
              [1, 0, 1],
              [4, -4, 5]])
tolerance = 1e-8
psi = np.array([1.0, 1.0, 1.0])
psi /= np.linalg.norm(psi)
ver=False
while ver!=True:
    psi_old = psi
    psi = np.linalg.solve(H, psi)
    psi /= np.linalg.norm(psi)
    if np.abs(np.dot(psi, psi_old)) > 1 - tolerance:
        ver=True
E0 = np.dot(psi, np.dot(H, psi))
print(f"Valor propio es: {ceil(E0)}")
print(f"Vector propio es: {psi}")

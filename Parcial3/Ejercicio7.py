import numpy as np
A = np.array([[3, -1, -1], [-1, 3, 1], [2, 1, 4]])
b = np.array([1, 3, 7])
x = np.array([0, 0, 0])
w = 1.2
max_iter = 1000
tol = 1e-6
for i in range(max_iter):
    x_prev = np.copy(x)
    for j in range(len(x)):
        x[j] = (1 - w) * x_prev[j] + (w / A[j, j]) * (b[j] - np.dot(A[j, :j], x[:j]) - np.dot(A[j, j+1:], x_prev[j+1:]))
    if np.linalg.norm(x - x_prev) < tol:
        print(f'Solución encontrada en {i} iteraciones:')
        print(x)
        break
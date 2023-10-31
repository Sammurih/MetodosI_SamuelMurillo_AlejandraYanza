A = [[1, 0, 0],[5,1,0],[-2,3,1]]

B = [[4, -2, 1],
    [0, 3, 7],
    [0, 0, 2]]
def multiplicar_matrices(a, b):
    filas_a, columnas_a = len(a), len(a[0])
    filas_b, columnas_b = len(b), len(b[0])
    c = [[0] * columnas_b for _ in range(filas_a)]
    for i in range(filas_a):
        for j in range(columnas_b):
            for k in range(columnas_a):
                c[i][j] += a[i][k] * b[k][j]
    return c
AB = multiplicar_matrices(A, B)
print(AB)
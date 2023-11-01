import numpy as np

generators = [np.array([[0,1],[1,0]]),
              np.array([[0,-1j],[1j,0]]),
              np.array([[1,0],[0,-1]])]

def commutator(A, B):
    return np.dot(A, B) - np.dot(B, A)

def levi_civita(i, j, k):
    if set((i, j, k)) == set((1, 2, 3)):
        return 1 if i == 1 else -1 if i == 3 else 0
    elif set((i, j, k)) == set((3, 2, 1)):
        return 1 if i == 3 else -1 if i == 1 else 0
    else:
        return 0

for i in range(3):
    for j in range(3):
        print(f"Conmutator con ({i+1},{j+1}):")
        print(commutator(generators[i], generators[j]), end="\n\n")

A = np.zeros((2,2)).astype(np.complex128)
for i in range(3):
    for j in range(3):
        for k in range(3):
            A += 2j*levi_civita(i+1,j+1,k+1)*generators[k]
        print(f"Conmutator con ({i+1},{j+1}):")
        print(A, end="\n\n")
        A = np.zeros((2,2)).astype(np.complex128)
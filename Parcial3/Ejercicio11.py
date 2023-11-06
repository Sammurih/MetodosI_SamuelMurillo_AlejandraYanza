import numpy as np

def MatrixMultiplication (A,B):
    mxn=np.shape(A)
    nxp=np.shape(B)
    
    if len(nxp)==1 and len(mxn)==1:
        C=np.dot(A,B)

    elif len(nxp)==1:
        C=np.zeros((mxn[0]))
        for i in range(0,mxn[0]):
            C[i]=np.dot(A[i,:],B)
    
    elif len(mxn)==1:
        C=np.zeros((mxn[0]))
        for i in range(0,mxn[0]):
            C[i]=np.dot(A,B[:,i])

    elif mxn[1]==nxp[0]:
        C=np.zeros((mxn[0],nxp[1]))
        for i in range(0,mxn[0]):
            for j in range(0,nxp[1]):
                C[i,j]=np.dot(A[i,:],B[:,j])

    else:
        return "Dimensiones incorrectas"
    return C

H = np.array([[1, 2, -1],
              [1, 0, 1],
              [4, -4, 5]])
Z=np.array([-1,-1,-1])
def Metodo_potencia (A,Z,k):
    for i in range(0,k):
        Z=Z/(np.sqrt(MatrixMultiplication(Z.T,Z)))
        Z=MatrixMultiplication(A,Z)
    W=Z/(np.sqrt(MatrixMultiplication(Z.T,Z)))   
    Vpropio=MatrixMultiplication(W.T,MatrixMultiplication(A,W))
    return Vpropio,W

P2=Metodo_potencia(np.linalg.inv(H),Z,55)
ValorPropioMin=1/(P2[0])
VectorPropioMin=P2[1]

print(ValorPropioMin,VectorPropioMin)


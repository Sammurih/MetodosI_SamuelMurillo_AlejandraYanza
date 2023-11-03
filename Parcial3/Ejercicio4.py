import numpy as np

A = np.array([[1,0,0],
              [5,1,0],
              [-2,3,1]])

B = np.array([[4,-2,1],
              [0,3,7],
              [0,0,2]])

def MatrixMultiplication (A,B):
    mxn=np.shape(A)
    nxp=np.shape(B)
    
    if len(nxp)==1:
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
AB = MatrixMultiplication(A,B)
print(AB)
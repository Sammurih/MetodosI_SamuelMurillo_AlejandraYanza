import numpy as np
import matplotlib.pyplot as plt

b = np.array([-3,-3,8,9])

A= np.array([[3,1,-1],
             [1,2,0],
             [0,1,2],
             [1,1,-1]])

def GetMinimosCuadradosMatrizVector(A,b):
    AT = np.dot(A.T,A)
    bT = np.dot(A.T,b)
    xsol = np.linalg.solve(AT,bT)
    return xsol

xsol=GetMinimosCuadradosMatrizVector(A,b)
print(xsol)
pw=np.dot(A, xsol)
print(np.round(pw,15))

MU=A.T
def Grand_Schmidt(MU):
    #print(np.shape(MU)[0])
    MV=np.empty((np.shape(MU)[0],np.shape(MU)[1]))
    for k in range(np.shape(MU)[0]):
        s=0
        #print(k)
        for j in range(0,k):
           #print(j)
           s+=np.dot((np.dot(MU[k],MV[j]))/(np.dot(MV[j],MV[j])),MV[j]) 
        MV[k]=MU[k]-s
        MV[k]=MV[k]/np.linalg.norm(MV[k])
    #print(MV,MU)
    return MV
MV=Grand_Schmidt(MU)
print(MV)

pw=0
for i in range(np.shape(MV)[0]):
    C=np.dot(b,MV[i])
    pw+=C*MV[i]
print(np.round(pw,15))
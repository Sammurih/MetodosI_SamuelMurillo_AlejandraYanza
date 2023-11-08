import numpy as np
A=np.array([[0.2,0.1,1,1,0],
           [0.1,4,-1,1,-1],
           [1,-1,60,0,-2],
           [1,1,0,8,4],
           [0,-1,-2,4,700]])
b=np.array([1,2,3,4,5])

def Descenso_Conjugado(A, b, x, e=0.01):
    r=np.matmul(A,x)-b
    p=-r
    k=0
    while np.max(np.abs(np.dot(A,x) - b)) > e:
        a=-(np.dot(r.T,p))/(np.matmul(np.matmul(p.T,A),p))
        x=x+a*p
        r=np.matmul(A,x)-b
        B=(np.matmul(np.matmul(r.T,A),p))/(np.matmul(np.matmul(p.T,A),p))
        p=-r+np.dot(B,p)

        k+=1
        
    return x,k

print(Descenso_Conjugado(A,b,np.array([0.,0.,0.,0.,0.])))
import numpy as np
import matplotlib.pyplot as plt

# Definamos el sistema usando una lista
A = np.array([lambda x,y: np.log(x**2+y**2)-np.sin(x*y)-np.log(2)-np.log(np.pi),
     lambda x,y: np.exp(x-y)+np.cos(x*y)])

B = np.array([lambda x,y,z: 6*x - 2*np.cos(y*z) - 1.,
     lambda x,y,z: 9*y + np.sqrt( x**2 + np.sin(z) + 1.06 ) + 0.9,
     lambda x,y,z: 60*z + 3*np.exp(-x*y)+10*np.pi - 3.])

def GetF(G,r):
    n = r.shape[0]
    v = np.zeros_like(r)
    if len(r) ==2:
        for i in range(n):
            v[i] = G[i](r[0],r[1])
    elif len(r) ==3:
        for i in range(n):
            v[i] = G[i](r[0],r[1],r[2])         
    return v

def GetJacobian(f,r,h=1e-6):
    n = r.shape[0]

    J = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            
            rf = r.copy()
            rb = r.copy()
            
            rf[j] = rf[j] + h
            rb[j] = rb[j] - h
            if len(r) ==2:
                J[i,j] = ( f[i](rf[0],rf[1]) - f[i](rb[0],rb[1])  )/(2*h)
            elif len(r) ==3:
                 J[i,j] = ( f[i](rf[0],rf[1],rf[2]) - f[i](rb[0],rb[1],rb[2])  )/(2*h)
    return J

def NewtonRaphson(G,r,itmax=1000,error=1e-9):
    it = 0
    d = 1.
    dvector = []
    while d > error and it < itmax:
        # Vector actual
        rc = r
        F = GetF(G,rc)
        J = GetJacobian(G,rc)
        InvJ = np.linalg.inv(J)
        r = rc - np.dot(InvJ,F)
        diff = r - rc
        d = np.max( np.abs(diff) )
        dvector.append(d)
        it += 1
    print(it)
    return r,dvector

r = NewtonRaphson(A,np.array([2.,2.]))[0]
print(r)
r = NewtonRaphson(B,np.array([0.,0.,0.]))[0]
print(r)

def Metric(G,r):
    return 0.5*np.linalg.norm(GetF(G,r))**2

def Minimizer(G,r,lr=1e-2,epochs=int(1e4),error=1e-7):
    
    metric = 1
    it = 0
    
    M = np.array([])
    R = np.array([r])
    
    while metric > error and it < epochs:
        
        M = np.append(M,Metric(G,r))
        
        J = GetJacobian(G,r)
        Vector = GetF(G,r)
        
        # Machine learning
        r -= lr*np.dot(J,Vector)
        
        R = np.vstack((R,r))
        
        metric = Metric(G,r)
        
        it += 1
    
    return r

r = Minimizer(A,np.array([2.,2.]))
print(r)
r = Minimizer(B,np.array([0.,0.,0.]))
print(r)
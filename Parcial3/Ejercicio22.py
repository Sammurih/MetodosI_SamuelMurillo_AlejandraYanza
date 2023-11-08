import numpy as np
import sympy as sym

x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)

def f(x,y):
    k=8.98755e9
    q=3e-4
    l=5
    w=114.6
    c=((k**2)*(q**4)*(1+2*sym.sqrt(2))**2)/((w**2)*(4**2)*(l**4)) #Aprox 0.07301955665405001
    z = x + sym.I*y
    f = (sym.sin(z))**6+c*(sym.sin(z))**2-c
    f = f.expand()
    return sym.re(f),sym.im(f)


f0,f1 = f(x,y)
F = [f0,f1]


J = sym.zeros(2,2)

for i in range(2):
    for j in range(2):
        if j==0:
            J[i,j] = sym.diff(F[i],x,1)
        else:
            J[i,j] = sym.diff(F[i],y,1)


InvJ = J.inv(method='LU')

Fn = sym.lambdify([x,y],F,'numpy')
IJn = sym.lambdify([x,y],InvJ,'numpy')


def NewtonRaphson(z,Fn,Jn,itmax=1000,precision=1e-10):
    
    error = 1
    it = 0
    
    while error > precision and it < itmax:
        
        IFn = Fn(z[0],z[1])
        IJn = Jn(z[0],z[1])
        
        z1 = z - np.dot(IJn,IFn)
        
        error = np.max( np.abs(z1-z) )
        
        z = z1
        it +=1
        
    #print(it)
    return z

z0 = np.array([-0.5,0 ])
z1 = np.array([0.5,0])
z2 = np.array([2,0])
z3 = np.array([4,0])
z4 = np.array([-0.5,-0.5])
z5 = np.array([-0.5,0.5])
z6 = np.array([0.5,-0.5])
z7 = np.array([0.5,0.5])
z8 = np.array([2.81,-0.56])
z9 = np.array([2.81,0.56])
z10 = np.array([3,-0.5])
z11 = np.array([3,0.5])
zsol0 = NewtonRaphson(z0,Fn,IJn)
print(zsol0)
zsol1 = NewtonRaphson(z1,Fn,IJn)
print(zsol1)
zsol2 = NewtonRaphson(z2,Fn,IJn)
print(zsol2)
zsol3 = NewtonRaphson(z3,Fn,IJn)
print(zsol3)
zsol4 = NewtonRaphson(z4,Fn,IJn)
print(zsol4)
zsol5 = NewtonRaphson(z5,Fn,IJn)
print(zsol5)
zsol6 = NewtonRaphson(z6,Fn,IJn)
print(zsol6)
zsol7 = NewtonRaphson(z7,Fn,IJn)
print(zsol7)
zsol8 = NewtonRaphson(z8,Fn,IJn)
print(zsol8)
zsol9 = NewtonRaphson(z9,Fn,IJn)
print(zsol9)
zsol10 = NewtonRaphson(z10,Fn,IJn)
print(zsol10)
zsol11 = NewtonRaphson(z11,Fn,IJn)
print(zsol11)


"""
def GetAllComplexRoots (Fn,Jn,tolerancia=10):
    N=1000
    Roots = np.zeros((N,2))
    x=np.linspace(0,2*np.pi,N)
    
    for i in range(N):
        z=[np.cos(x[i]),np.sin(x[i])]
        root = NewtonRaphson(z,Fn,Jn)
        Roots[i,0]=root[0]        
        Roots[i,1]=root[1]
        
    Roots=np.unique(Roots,axis=0)

    for i in range(Roots.shape[0]):
        Roots[i,0]=np.round(Roots[i,0]%, tolerancia)
        Roots[i,1]=np.round(Roots[i,1], tolerancia)
    Roots=np.unique(Roots,axis=0)
    Roots=np.unique(Roots,axis=1)
    
        croot = np.round(root, tolerancia)
            
        if not any(np.array_equal(croot, root) for root in Roots):    
            Roots.append(croot)
    for i in range(len(Roots)):
        Roots[i][0]=Roots[i][0]%2*np.pi
    
    return Roots
print("###")
Roots=GetAllComplexRoots(Fn,IJn)
for i in range(len(Roots)):
    print(Roots[i])
"""
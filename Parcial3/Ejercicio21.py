import numpy as np
import sympy as sym
x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)
def f(x,y):
    k=8.98755e9
    q=3e-4
    l=5
    w=114.6
    c=((k**2)*(q**4)*(3+6*sym.sqrt(2))**2)/((w**2)*(4**2)*(l**4))
    z = x + sym.I*y
    f = (sym.sin(z))**6+c*(sym.sin(z))**2-c
    f = f.expand()
    return sym.re(f),sym.im(f)


f0,f1 = f(x,y)
F = [f0,f1]
print(F)
J = sym.zeros(2,2)

for i in range(2):
    for j in range(2):
        if j==0:
            J[i,j] = sym.diff(F[i],x,1)
        else:
            J[i,j] = sym.diff(F[i],y,1)

#print(J)
InvJ = J.inv(method='LU')
#print(InvJ)

Fn = sym.lambdify([x,y],F,'numpy')
IJn = sym.lambdify([x,y],InvJ,'numpy')
#print(IJn(1.,1.))

def NewtonRaphson(z,Fn,Jn,itmax=100,precision=1e-9):
    
    error = 1
    it = 0
    
    while error > precision and it < itmax:
        
        IFn = Fn(z[0],z[1])
        IJn = Jn(z[0],z[1])
        
        z1 = z - np.dot(IJn,IFn)
        
        error = np.max( np.abs(z1-z) )
        
        z = z1
        it +=1
        
    print(it)
    return z
z0 = np.array([1,-2])
zsol = NewtonRaphson(z0,Fn,IJn)
print(zsol)

x,y=zsol
k=8.98755e9
q=3e-4
l=5
w=114.6
c=((k**2)*(q**4)*(3+6*2**(1/2))**2)/((w**2)*(4**2)*(l**4))
z = x + sym.I*y
f = (sym.sin(z))**6+c*(sym.sin(z))**2-c

print(sym.simplify(f))
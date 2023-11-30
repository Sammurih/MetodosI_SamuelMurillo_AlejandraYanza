import sympy as sp

x, y, z, l = sp.symbols('x y z l')

f = x**2 + y**2 + z**2 - 2*z + 1
g = 2*x - 4*y + 5*z - 2

ec1 = sp.diff(f, x) - l * sp.diff(g, x)
ec2 = sp.diff(f, y) - l * sp.diff(g, y)
ec3 = sp.diff(f, z) - l * sp.diff(g, z)

sol = sp.solve([ec1, ec2, ec3, g], (x, y, z, l))
val_min = f.subs({x: sol[x], y: sol[y], z: sol[z]})

print(val_min)
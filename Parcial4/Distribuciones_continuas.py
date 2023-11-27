import sympy as sp

x, y = sp.symbols('x y')

f = 2/3 * (x + 2*y)

non_negativity = sp.integrate(f, (x, 0, 1), (y, 0, 1))
non_negativity_condition = non_negativity >= 0

integration = sp.integrate(f, (x, 0, 1), (y, 0, 1))
integration_condition = sp.simplify(integration) == 1

print("No negatividad:", non_negativity_condition)
print("Integración unitaria:", integration_condition)

g = sp.integrate(f, (y, 0, 1))

h = sp.integrate(f, (x, 0, 1))

print("Distribución marginal g(x):", g)
print("Distribución marginal h(y):", h)
    
E_x = sp.integrate(x * f, (x, 0, 1), (y, 0, 1))

print("(E(X)):", E_x)

E_y = sp.integrate(y * f, (x, 0, 1), (y, 0, 1))

print("(E(Y)):", E_y)

E_xy = sp.integrate(x * y * f, (x, 0, 1), (y, 0, 1))
cov_xy = E_xy - E_x * E_y


print("σxy:", cov_xy)

E_xy = sp.integrate((x - E_x) * (y - E_y) * f, (x, 0, 1), (y, 0, 1))

print("σxy:", E_xy)

independence = sp.simplify(f - g * h) == 0

if independence:
    print("X e Y son independientes.")
else:
    print("X e Y no son independientes.")
     
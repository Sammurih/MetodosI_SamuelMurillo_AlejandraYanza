from sympy import exp, diff, solve, factorial, symbols
x=symbols("x")
for i in range(20):
    L_i = exp(x) / factorial(i) * diff(exp(-x) * x**i, x, i)
    roots = solve(L_i, x, domain=(0, float('inf')))
    roots = [root.evalf() for root in roots] 
    print(f"LAS RACICES DEL POLINOMIO DE LAGUERRE L_{i}(x) son: ({', '.join(map(str, roots))})\n")
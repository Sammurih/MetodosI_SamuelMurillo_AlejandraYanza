from scipy.optimize import minimize

def f_obj(var):
    x, y, z = var
    return -x * y * z
def f_restr(var):
    x, y, z = var
    return x * y + 2 * y * z + 2 * x * z - 12
v0 = [1, 1, 1]
restric = {'type': 'eq', 'fun': f_restr}
resp = minimize(f_obj, v0, constraints=restric)
print(-resp.fun)
print(resp.x)
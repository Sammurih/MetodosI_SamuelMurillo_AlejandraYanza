import numpy as np

def integrate(n):
    m=np.zeros((n+1,n+1))
    for i in range(n+1):
        for j in range(n+1):
            val=1-(i*2/n**2)-(j**2/n*2)
            if val>=0:
                m[i][j]=np.sqrt(val)

    xis=len(m)
    yis=len(m[0])            
    v = 0.0
    for i in range(xis-1):
        for j in range(yis-1):
            avg_value = (m[i][j]) + m[i+1][j]+m[i][j+1]+m[i+1][j+1]
            
            
            v += avg_value/n**2

    return v
print(integrate(1000))
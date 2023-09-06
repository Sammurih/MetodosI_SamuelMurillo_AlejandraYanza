import numpy as np

def diferencia_div_2 (x0, x1, F):
    resul= (F(x1)-F(x0))/(x1-x0)
    return resul

def diferencia_div_3(x0,x1,x2,F):
    resul= (diferencia_div_2(x1,x2,F)- diferencia_div_2(x0,x1,F))/(x2-x0)
    return resul

def define_abc(x0,x1,x2,F):
    a=diferencia_div_3(x0,x1,x2,F)
    b=diferencia_div_2(x0,x1,F)-((x0+x1)*(diferencia_div_3(x0,x1,x2,F)))
    c=F(x0)-((x0)*diferencia_div_2(x0,x1,F))+(x0*x1*diferencia_div_3(x0,x1,x2,F))

    return np.array[a,b,c]

    
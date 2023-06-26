import numpy as np
from sympy import *

def trap(f,a,b,d = 4,n = 1):
    '''
    Params:
    f >> f(x) passagem por lambda ou valor vetorizado
    a,b >> intervalo da integral
    N >> número de trapezios
    d >> número de casas decimais para arredondamento
    
    '''

    x = np.linspace(a,b,n+1)
    y = f(x)
    yd = y[1:]
    ye = y[:-1]
    dx = (b-a)/n
    result = (dx/2) * np.sum(yd+ye)


    result = f'{result:.{d}f}'
    return result



def err_t(f,a,b,d,n):
    '''
    params:
    f >> f(x) passagem por lambda ou valor vetorizado
    N >> número de trapezios
    d >> número de casas decimais para arredondamento
    '''


    #Erro de arredondamento
    if d == 0:
        d_err = 0
    else:
        d_err = 0.05
        for i in range(d-1):
            d_err = d_err/10

    
    aux = np.linspace(a,b,n+1)
    ampl = aux[1] - aux[0]
    d_err = d_err * ampl
    d_err = d_err * n


    #Erro de truncamento

    aux2 = (ampl**3)/12
    
    x = Symbol('x')
    f_first = f.diff(x)

    f_second = f_first.diff(x)
    f_second = sqrt(f_second **2)


    x_max = maximum(f_second,x,Interval(a,b))

    t_err = aux2 * x_max

    t_err = t_err * n


    err_total = float(t_err) + float(d_err)

    err_total = f'{err_total:.6f}'

    return err_total
    
    


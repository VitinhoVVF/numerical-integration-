from trap import trap as tr
from trap import err_t as err
import numpy as np
from sympy import *

#Testes

# 1-  integral 2 - 5 : raiz(x) com 5 decimais e 1 trapezio
test1 = tr(lambda x : np.sqrt(x),2,5,5,1)
print("Resultado 1 >> "+test1)

x = Symbol('x')
err1 = err(sqrt(x),2,5,5,1)
print("Erro trap >>",err1)
print(test1, "+|-", err1)
print(test1 == '5.47542')



print()

# 2 - integral 2 - 5 : raiz(x) com 3 decimais e 6 trapezios
test2 = tr(lambda x : np.sqrt(x),2,5,3,6)
print("Resultado 2 >> " + test2)
err2 = err(sqrt(x),2,5,3,6)
print("Erro trap >>",err2)
print(test2, "+|-", err2)
print(test2 == '5.565')

print()

# 3 - integral 1.5 - 2.5: e^(-(t^2)/2) / sqrt(2*pi) 4 decimais e 1 trapezio
test3 = tr(lambda t: (np.e ** (-(t**2)/2)) / (np.sqrt((2*np.pi))), 1.5, 2.5)
print("Resultado 3 >> " + test3)
err3 = err((np.e ** (-(x**2)/2)) / (np.sqrt((2*np.pi))),1.5,2.5,4,1)
print("Erro trap >>",err3)
print(test3, "+|-", err3)
print(test3 == '0.0735')

print()

# 4 - integral 1.5 - 2.5: integral 1.5 - 2.5: e^(-(t^2)/2) / sqrt(2*pi) 5 decimais e 11 trapezios
test4 = tr(lambda t: (np.e ** (-(t**2)/2)) / (np.sqrt((2*np.pi))), 1.5, 2.5,5,10)
print("Resultado 4 >> " + test4)
err4 = err((np.e ** (-(x**2)/2)) / (np.sqrt((2*np.pi))),1.5,2.5,5,10)
print("Erro trap >>",err4)
print(test4, "+|-",err4)
print(test4 == '0.06072')

print()

# 5 - integral 6 - 10: log(x)
test5 = tr(lambda x : np.log(x),6,10,8,8)
print("Resultado 5 >> " + test5)
err5 = err(log(x),6,10,8,8)
print(test5,"+|-",err5)
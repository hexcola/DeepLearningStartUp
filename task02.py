# python 3.6
from sympy import Symbol, sin, Derivative

x = Symbol('x')
y = sin(x**2)*x
d = Derivative(y, x)
print(d.doit())


# This file won't be used 
import sympy as sp
from scipy.misc import derivative
from multipledispatch import dispatch 
def f(x):
    return 3*x**2 + 1
@dispatch()
def fd():
    x = sp.Symbol('x')
    return sp.diff(f(x), x)
@dispatch(float)
def fd(x):
    return derivative(f, x)

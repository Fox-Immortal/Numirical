import math
import sympy as sp
from scipy.misc import derivative
from multipledispatch import dispatch 
from prettytable import PrettyTable

d = 4

def f(x):
    return x**3 - 2 * x ** 2 + x - 3
@dispatch()
def fd():
    x = sp.Symbol('x')
    print(sp.diff(f(x), x))
    return sp.diff(f(x), x)
@dispatch(float)
def fd(x):
    return round(derivative(f, x, dx=1e-6), d)

class newton():

    def __init__(self, _xi, _target_error, _end):
        
        self.xi = _xi * 1.0
        self.target_error = _target_error
        self.end = _end
        self.save = [self.xi, self.target_error, self.end]
        self.error = -1
        self.iteration = 0
        self.xi_1 = 0
        self.fx = 0
        self.fdx = 0
        self.table = PrettyTable()
        self.table.field_names = ["iteration", "Xi", "fx", "fdx", "Xi+1", "error"]
    def do_newton(self):
        if(self.iteration == self.end or (self.error <= self.target_error and self.error != -1)):
            print(self.table)
            return
        self.fx = round(f(self.xi), d)
        self.fdx = round(fd(self.xi), 4)
        self.xi_1 = round(self.xi - self.fx/self.fdx, 4)
        self.error = round(abs(self.xi_1 - self.xi)/self.xi * 100, 4)
        self.table.add_row([self.iteration, self.xi, self.fx, self.fdx, self.xi_1, self.error])
        self.iteration += 1
        if(self.error > 100):
            print("There are no zeros diverge")
            return
        self.xi = self.xi_1
        self.do_newton()
    def reset(self):
        self.xi = self.save[0]
        self.target_error = self.save[1]
        self.end = self.save[2]
        self.table = PrettyTable()
        self.error = -1
        self.iteration = 0
        self.xi_1 = 0
        self.fx = 0
        self.fdx = 0
    def do_newton_m(self, m):
        if(self.iteration == self.end or (self.error <= self.target_error and self.error != -1)):
            print(self.table)
            return
        self.fx = round(f(self.xi), d)
        self.fdx = round(fd(self.xi), 4)
        self.xi_1 = round(self.xi - m * (self.fx/self.fdx), 4)
        self.error = round(abs(self.xi_1 - self.xi)/self.xi * 100, 4)
        self.table.add_row([self.iteration, self.xi, self.fx, self.fdx, self.xi_1, self.error])
        self.iteration += 1
        if(self.error > 100):
            print("There are no zeros diverge")
            return
        self.xi = self.xi_1
        self.do_newton_m(m)

s = newton(4, 1, 10)
s.do_newton()

        

import math
import sympy as sp
from scipy.misc import derivative
from multipledispatch import dispatch 
from prettytable import PrettyTable

d = 4

def f(x):
    return math.exp(x * -1.0) - x

class secant():

    def __init__(self, _xi__1, _xi, _target_error, _end):
        self.xi__1 = _xi__1
        self.xi = _xi
        self.target_error = _target_error
        self.end = _end
        self.error = -1
        self.iteration = 0
        self.fx = 0
        self.fx__1 = 0
        self.table = PrettyTable()
        self.table.field_names = ["iteration", "Xi-1", "fx-1", "Xi", "fx", "Xi+1", "error"]

        
    def do_secant(self):
        if(self.iteration == self.end or (self.error <= self.target_error and self.error != -1)):
            print(self.table)
            return
        self.fx__1 = f(self.xi__1)
        self.fx = f(self.xi)
        self.xi_1 = self.xi - ((self.fx * (self.xi__1 - self.xi))/(self.fx__1 - self.fx))
        self.error = round(abs(self.xi_1 - self.xi)/self.xi_1 * 100, 4)
        self.table.add_row([self.iteration, self.xi__1, self.fx__1, self.xi, self.fx, self.xi_1, self.error])
        self.iteration += 1
        if(self.error > 100):
            print(self.table)
            print("There are no zeros diverge")
            return
        self.xi__1 = self.xi
        self.xi = self.xi_1
        self.do_secant()

s = secant(0, 1, 0, 10)
s.do_secant()

        























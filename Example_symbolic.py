#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:45:48 2021

@author: arahman
"""


from sympy import *

x = Symbol('x')
y = Symbol('y')

print (2*x + 3*x - y)               # Algebraic expression
print (diff(x**2, x))               # Differentiate w.r.t. x
print (integrate(sin(x), x))        # Integrate w.r.t. x
print (simplify((x**2 + x**3)/x**2)) # Simplifies expression
print (limit(sin(x)/x, x, 0))        # Finds limit of sin(x)/x as x->0
print (solve(5*x - 15, x))           # Solves 5*x = 15
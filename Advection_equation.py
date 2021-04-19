#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 19:27:14 2021

@author: arahman
"""

# Numerical solution of the linear advection equation #ut+ux=0
# using *centered difference* for u x => NAIVE
# periodic boundaray data
from numpy import *
import matplotlib.pyplot as plt


# Initial condition 

def u0(x):
     return where(abs(x)<=1, 1.0 , 0.0)


# Spatial domain [=L, L] and time [0, T] L=5.

T=1.

# Discretization parameters h, dt

h=0.1
dt = 0.1

# Grid ratio

gam = dt/h

# number of space and time steps

n = int(2*L/h)+1
m=int(T/dt)

# Initialize

x = linspace(-L,L,n)
u = u0(x)

# Plot

plt.close('all')
   
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 19:27:14 2021

@author: arahman
"""

# Numerical solution of the linear advection equation #ut+ux=0
# using *centered difference* for u_x => NAIVE
# periodic boundaray data


from numpy import *
import matplotlib.pyplot as plt

def u0(x):                  # Initial condition 
    return where(abs(x) <= 1, 1.0 , 0.0)

# Spatial domain [-L, L] and time [0, T] 

L = 5.
T = 1.
h = 0.1                     # Discretization parameters h, dt
dt = 0.1

gam = dt/h                  # Grid ratio
n = int(2*L/h)+1            # number of space and time steps
m = int(T/dt)
x = linspace(-L, L, n)      # Initialize
u = u0(x)

plt.close('all')
plt.figure(1)
fig, ax = plt.subplots(num = 1)
ax.set(xlim = (-L, L), ylim = (-1, 2), xlabel='x', ylabel= 'u')
l1, = ax.plot(x, u, 'b-')
l2, = ax.plot(x, u0(x), 'r-')
t1 = ax.text(3, 1.7, 't=0.00')
ax.grid ()

for k in linspace(dt, T, m):
    u[1: -1] = u[1: -1] - gam*(u[2:] - u[0: -2]) /2      # Compute solution at new time level
    u[0] = u[0] - gam*(u[1] - u[-1])/2       # Boundary data
    u[-1] = u[-1] - gam*(u[0] - u[-2])/2
    l1.set_ydata(u)
    l2.set_ydata(u0(x-k))
    t1.set_text('t = %5.2f'  %k)
    plt.draw()
    plt.pause(0.2)

#fig.savefig ('naive1.eps')
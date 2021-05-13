#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 17:03:58 2021

@author: arahman
"""

# Numerical solution of the linear advection equation : ut+ux=0
# using Lax-Friedrichs and periodic boundaray data


from numpy import *
import matplotlib.pyplot as plt

def u0(x):
    # sin(2*pi*x/L)+sin(4*pi*x/L)
    return where(abs(x + 1) <= 1, 1.0 , 0.0)
    # return exp(-x**2)
# Flux
def f(u):
    return u

# Spatial domain [-L, L] and time [0, T] 

L = 5.01
T = 3.

c = 1.                      # Advection velocity

h = 0.1                     # Discretization parameters h, dt
dt = 0.05

gam = dt/h                  # Grid ratio
n = int(2*L/h)+1            # number of space and time steps
m = int(T/dt)

x = linspace(-L, L, n)      # Initialize
u = u0(x)
un = u0(x)

plt.close('all')
plt.figure(1)
fig, ax = plt.subplots(num = 1)
ax.set(xlim = (-L, L), ylim = (-.5, 1.5), xlabel = 'x', ylabel = 'u')
l1, = ax.plot(x, u, 'b-')
l2, = ax.plot(x, u0(x), 'r--')
k = 0
t1 = ax.text(3, 1.3, 't = %5.2f' %k)
ax.grid ()
plt.show()

for k in linspace(dt, T, m):
    u[1:-1] = (u[2:]+ u[0:-2])/2. - gam*(f(u[2:]) - f(u[0: -2]))/2.     # Compute solution at new time level
    u[0] = (u[1] + u[-1])/2. - gam*(f(u[1]) - f(u[-1]))/2.       # Boundary data
    u[-1] = (u[0] + u[-2])/2. - gam*(f(u[0]) - f(u[-2]))/2.
    u = un[:]
     
    l1.set_ydata(u)
    l2.set_ydata(u0(x-k))
    t1.set_text('t = %5.2f'  %k)
    plt.draw()
    plt.pause(0.3)
    
#fig.savefig ('Lax-Friedrichs1.eps')
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 19:51:49 2021

@author: arahman
"""

# Explicit discretization of the diffusion equation
# u_t = u_xxx + f

from numpy import *
import matplotlib.pyplot as plt

# Domain & discretization
L = 2.0
h = 0.05
n = int(L/h) + 1
x = linspace(0, L, n)
T = 1
tau = 0.00125
gam = tau/(h**2)
print('gamma = %6.4f' % gam)
m = int(T/tau)
t = linspace(tau, T, m)


def u0(x):
    return zeros_like(x)
    #return where(abs(x-0.5)<=0.25, 1.0, 0.0)


def f(t, x):
    return (1 + pi*pi*t)*sin(pi*x)


tt = 0
u = u0(x)

plt.close('all')
fig, ax = plt.subplots(num = 1)
ax.set_ylim((-1.1, 1.1))
l1, = ax.plot(x, u, 'b-')
l2, = ax.plot(x, u, 'r.')
ax.text(1.55, 0.85, 'tau = %6.5f' %tau)
txt = ax.text(1.62, 0.75, 't = %5.3f' %tt)
ax.grid ()
plt.show()


unew = zeros_like(u)
for tt in t:
    unew[1: -1] = u[1: -1] + gam*(u[0: -2] - 2*u[1: -1] + u[2:]) + tau*f(tt, x[1: -1])
    # Dirrichlet boundary conditions
    unew[0] = 0.0
    unew[-1] = 0.0
    #plot new solution
    l1.set_ydata(unew)
    l2.set_ydata(tt*sin(pi*x))
    txt.set_text('t = %5.2f' %tt)
    plt.draw()
    plt.pause(0.1)
    u = unew.copy()
    
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


# Spatial domain [-L, L] and time [0, T] 

L=5.
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
plt . figure (1)
fig ,ax= plt.subplots(num=1)
ax.set(xlim=(=L,L), ylim=(=1,2), xlabel=’x’, ylabel=’u’) l1,=ax.plot(x,u, ’b=’)
t1 = ax.text(3,1.7,’t=0.00’)
ax . grid ()
for k in linspace(dt,T,m):
# Compute solution at new time level
u[1: =1] = u[1:=1]=gam*(u[2:] =u[0: =2]) /2. # boundary data
u[0] = u[0]=gam*(u[1]=u[=1])/2. u[=1] = u[=1]=gam*(u[0]=u[=2])/2.
# and plot it
l1 . set ydata (u)
t1.set text(’t=%5.2f’ %k) plt .draw()
plt . pause (0.01)
fig . savefig ( ’naive1 . eps ’)
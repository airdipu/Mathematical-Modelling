#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 23:22:19 2021

@author: arahman
"""

from numpy import linspace
import matplotlib.pyplot as plt

v0 = 5              # Initial velocity
g = 9.81            # Acceleration
t = linspace(0, 1, 1001)
y = v0*t - (1/2)*g*t**2
print(y)
plt.plot(t, y)
plt.xlabel('t (s)')
plt.ylabel('y (m)')
plt.show()
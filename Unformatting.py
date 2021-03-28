#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 23:54:12 2021

@author: arahman
"""

from math import sin
t0 = 2
dt = 0.55
# Unformatted print
 
t = t0 + 0*dt; g = t*sin(t)
print (t, g)
t = t0 + 1*dt; g = t*sin(t)
print (t, g)
t = t0 + 2*dt; g = t*sin(t)
print (t, g)
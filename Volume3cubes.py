#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 21:31:41 2021

@author: arahman
"""


# if L is an array with three elements. That is, compute V for each value of L. 
# c) In a program, write out the result V of V=L**3 when L is an array with 
# three elements as computed by linspace in a). Compare the resulting volumes 
# with your hand calculations. d) Make a plot of V versus L



from numpy import *
import matplotlib.pyplot as plt


L = linspace(1, 3, 3)
V = L**3                # Volume of a cube

plt.plot(L, V)
print(V)
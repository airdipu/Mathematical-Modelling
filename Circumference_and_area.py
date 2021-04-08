#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 21:15:49 2021

@author: arahman
"""

# Write a program that computes both the circumference C and the area A 
# of a circle with radius r = 2 cm. Let the results be printed to the screen
#  on a single line with an appropriate text. The variables C, A and r should 
# all be defined as a separate variables in the program. Run the program and
# confirm that the correct results are printed.
# Filename: circumference_and_area.py.

from math import *

r = 2                   # radius of a circle
c = 2*pi*r              # circumference of a circle
a = pi*r**2             # area of a circle
#c, a = symbols('c a')
print("Circumference of a circle", c, "and Area of a circle", a)

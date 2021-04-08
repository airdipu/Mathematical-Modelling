#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 21:02:07 2021

@author: arahman
"""

# Write a program that computes the volume V of a cube with sides of 
# length L = 4 cm and prints the result to the screen. Both V and L 
# should be defined as separate variables in the program. Run the program 
# and confirm that the correct result is printed.


from sympy import *

l, v = symbols('l v') 
l = 4.0                   # lengths of a side
v = l**3                # formulae for calculating the volume
print('The lengths of side is ', l)
print('The volume is', v)

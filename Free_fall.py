#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 21:27:40 2021

@author: arahman
"""
# Program for computing the height of a ball in vertical motion


v0 = 5          # Initial velocity
g = 9.81        # Acceleration of gravity
t = 0.6         # Time

y = v0*t - 0.5*g*t**2        # Vertical position

print (y)

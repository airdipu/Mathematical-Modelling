#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 00:38:59 2021

@author: arahman
"""

# Population model using Upwind scheme
# pt + px = −μp

from numpy import *
import matplotlib.pyplot as plt


MAXAGE = 160
dx = 1
dt = 0.4
gam = dt/dx
MAXTIME = 60


n = int(MAXAGE/dx) + 1
x = linspace (0, MAXAGE, n)
m = int(MAXTIME/dt)
t = linspace(dt, MAXTIME, m)


mu = log(2)/25.0

def p0(x):
    # Initial age profile
    return where( x <=  80, 2.0E4*(1 - x/80.0), 0.0)


def birth(t):
    # number newborns at time t
    return 9250.0
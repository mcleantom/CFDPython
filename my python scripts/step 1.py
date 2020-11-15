# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:41:05 2020

@author: mclea
"""

import numpy as np
import matplotlib.pyplot as plt
import time, sys

nx = 100         # The number of grid points
dx = 2/(nx-1)   # The distance between grid points
nt = 80         # The number of time steps to calculate
dt = 0.0025      # The time step
c = 1           # The wave speed

u = np.ones(nx)*-1
u[int(.5/dx):int(1/dx + 1)] = 2

plt.plot(np.linspace(0, 2, nx), u)

un = np.ones(nx)

for n in range (nt):
    un = u.copy()
    for i in range(1, nx):
        u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])
        
plt.plot(np.linspace(0, 2, nx), u)
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 11:47:36 2020

@author: mclea
"""
import numpy as np
import matplotlib.pyplot as plt

sigma = 0

# Set up a grid
# Number of sub-intervals
n = 1000
n += 1
h = 1/n
L = 1
x = np.linspace(0, L, n)

# The slope
f = np.ones(n)
# f[int(n/2):] = -1
f = np.vstack(f)

# Approximation to the exact solution
v = np.vstack(np.zeros(n))

A = np.zeros((n,n))
np.fill_diagonal(A, (2+sigma*h**2))
rng = np.arange(n-1)
A[rng, rng+1] = -1
rng = np.arange(n)
A[rng, rng-1] = -1
A = (1/h**2)*A

# Calculate the residual
r = f - np.dot(A, v)

# Calculate the error
e = np.dot(np.linalg.inv(A), r)

u = v + e

plt.plot(x, u)

du = np.diff(u, prepend=0, axis=0)/h
ddu = np.diff(du, prepend=0, axis=0)/h
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:58:24 2020

@author: mclea
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy
from sympy import init_printing
init_printing(use_latex=True)

x, nu, t = sympy.symbols('x nu t')
phi = (sympy.exp(-(x-4*t)**2 / (4*nu*(t+1))) +
       sympy.exp(-x(x - 4 * t - 2 * sympy.pi)**2 / (4 * nu * (t+1))))

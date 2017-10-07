# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 16:35:05 2017

@author: julie
"""

import numpy as np
from numpy import *
import math
from math import *
import matplotlib.pyplot as plt
n=1000
T=100
t=np.linspace(0,T,n)
k=T/n
b=1
a=1
c=1
m=1
M=5
K=(4*pi*pi*m)/(a*a*t*t+2*a*b*t+b*b)
r_0=np.zeros(n)
for i in range(n):
    r_0[i] = sqrt((c*c/K[i])*M)
    
r=np.zeros(n)
r_dot=np.zeros(n)

r[0]=r_0[0]
r_dot[0]=1

for i in range(1,n):
    r[i]= r[i-1] + k*r_dot[i-1]
    r_dot[i]=r_dot[i-1]+k*(-(K[i-1]/m)*(r[i-1]-r_0[i-1]))*r[i-1]
    
print(r)
print(r_dot)
    
plt.plot(t,r)
plt.xlabel('time')
plt.ylabel('radius')


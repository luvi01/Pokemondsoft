#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 14:36:57 2018

@author: luvi
"""
import math as m
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
G=6.674*10**-11
M=1.9891*10**30
P=3.155*10**7
L=1.496*10**11
    
    
def EquacoesDiferenciais(lisSolucoes, t):
    x=lisSolucoes[0]
    Vx=lisSolucoes[1]
    y=lisSolucoes[2]
    Vy=lisSolucoes[3]
    dxdt=Vx 
    dVxdt=(-(G*M*P**2)/L**3)*x/((x**2)+(y**2))**(3/2)
    dydt=Vy
    dVydt=(-(G*M*P**2)/L**3)*y/((x**2)+(y**2))**(3/2)
    
    return[dxdt,dVxdt,dydt,dVydt]
    
x=1
y=0
Vx=0
Vy=2*m.pi
Y0=[x,Vx,y,Vy]
t=np.arange(0,1,10**-4)

S=odeint(EquacoesDiferenciais, Y0, t)
X=S[:,0]
Y=S[:,2]


plt.plot(Y,X)
plt.ylabel('Energia (J)')
plt.xlabel('Tempo (s)')
plt.grid(True)
plt.show()

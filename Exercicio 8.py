# -*- coding: utf-8 -*-
"""
Created on Tue May 29 18:32:38 2018

@author: luvi01
"""

from scipy.integrate import odeint
import numpy as np
import math
import matplotlib.pyplot as plt
p = 1
r = 0.1
Cd = 1.5
A = math.pi*r**2
g = 10
m = 0.2
K = 20
l = 0.5
AT = 0.001
t = np.arange(0,5,AT)

def EquacoesDiferenciais(listaSolucoes, t):
    X=listaSolucoes[0]
    Y=listaSolucoes[1]
    Vx=listaSolucoes[2]
    Vy=listaSolucoes[3]
    
    COSSENO = (Y/math.sqrt((Y**2)+(X**2)))
    SENO = (X/math.sqrt((Y**2)+(X**2)))
    Felx = ((K*(math.sqrt((Y**2)+(X**2))-l))*SENO)
    Fely = ((K*(math.sqrt((Y**2)+(X**2))-l))*COSSENO)
    Fresx = (((1/2)*p*Cd*A*((Vy**2)+(Vx**2)))*SENO)
    Fresy = (((1/2)*p*Cd*A*((Vy**2)+(Vx**2)))*COSSENO)   
    
    dXdt=Vx
    dYdt=Vy
    dVxdt = (- Felx - Fresx)/m
    dVydt = (- Fely - Fresy- m*g)/m
    # vamos considerar que tudo para ao atingir o chão
    
    return [dXdt, dYdt, dVxdt, dVydt]


S0 = [0.55,0,0,0]
S=odeint(EquacoesDiferenciais, S0, t)
plt.plot(S[:,0], S[:,1])
plt.title('PRIMEIRA SITUAÇÃO COM RESISTENCIA DO AR')
plt.ylabel("Y")
plt.xlabel("X")
plt.grid(True)
plt.show()

plt.plot(t, S[:,0])
plt.title('PRIMEIRA SITUAÇÃO COM RESISTENCIA DO AR (Abscissa)')
plt.ylabel("X")
plt.xlabel("t")
plt.grid(True)
plt.show()

plt.plot(t, S[:,1])
plt.title('PRIMEIRA SITUAÇÃO COM RESISTENCIA DO AR (Ordenada)')
plt.ylabel("Y")
plt.xlabel("t")
plt.grid(True)
plt.show()

#=====================================================
Cd = 0
S=odeint(EquacoesDiferenciais, S0, t)

plt.plot(S[:,0], S[:,1])
plt.title('PRIMEIRA SITUAÇÃO SEM RESISTENCIA DO AR')
plt.ylabel("Y")
plt.xlabel("X")
plt.grid(True)
plt.show()

plt.plot(t, S[:,0])
plt.title('PRIMEIRA SITUAÇÃO SEM A RESISTENCIA DO AR (Abscissa)')
plt.ylabel("X")
plt.xlabel("t")
plt.grid(True)
plt.show()

plt.plot(t, S[:,1])
plt.title('PRIMEIRA SITUAÇÃO SEM A RESISTENCIA DO AR (Ordenada)')
plt.ylabel("Y")
plt.xlabel("t")
plt.grid(True)
plt.show()
#====================================================
p = 1
r = 0.01
Cd = 1.5
A = math.pi*r**2
g = 10
m = 0.2
K = 20
l = 0.5
S=odeint(EquacoesDiferenciais, S0, t)
plt.plot(S[:,0], S[:,1])
plt.title('SEGUNDA SITUAÇÃO COM RESISTENCIA DO AR')
plt.ylabel("Y")
plt.xlabel("X")
plt.grid(True)
plt.show()

plt.plot(t, S[:,0])
plt.title('SEGUNDA SITUAÇÃO COM RESISTENCIA DO AR (Abscissa)')
plt.ylabel("X")
plt.xlabel("t")
plt.grid(True)
plt.show()

plt.plot(t, S[:,1])
plt.title('SEGUNDA SITUAÇÃO COM RESISTENCIA DO AR (Ordenada)')
plt.ylabel("Y")
plt.xlabel("t")
plt.grid(True)
plt.show()

#=====================================================
Cd = 0
S=odeint(EquacoesDiferenciais, S0, t)

plt.plot(S[:,0], S[:,1])
plt.title('SEGUNDA SITUAÇÃO SEM RESISTENCIA DO AR')
plt.ylabel("Y")
plt.xlabel("X")
plt.grid(True)
plt.show()

plt.plot(t, S[:,0])
plt.title('SEGUNDA SITUAÇÃO SEM A RESISTENCIA DO AR (Abscissa)')
plt.ylabel("X")
plt.xlabel("t")
plt.grid(True)
plt.show()

plt.plot(t, S[:,1])
plt.title('SEGUNDA SITUAÇÃO SEM A RESISTENCIA DO AR (Ordenada)')
plt.ylabel("Y")
plt.xlabel("t")
plt.grid(True)
plt.show()



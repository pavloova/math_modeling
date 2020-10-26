import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
from math import sqrt
phi = np.linspace(0, 2*np.pi, 1000)  

def light(q, phi):
    V=sqrt((G*m/a)* ((1+e)/(1-e)))
    dWdt=(L*s)/(4*np.pi*q*V)   
    return dWdt
e=0.02
G=6.67*10**(-11)
m=1.989*10**30
a=149000000000
L=3.89*10**26
s=np.pi*6400000**2
q0=a*(1-e)

vel = odeint(light,q0,phi)
plt.plot(phi,vel[:,0],label='световая энергия')
plt.grid() 
plt.legend()

plt.show()


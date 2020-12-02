import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 

t=np.arange(1,100,0.01)
def rasp(z,t):
    x,y=z
    dxdt=k1*(A0-x-y)
    dydt=k2*(A0-x-y)
    return dxdt,dydt
A0=10
x0=0
y0=0
k1=0.2
k2=0.1
z0=x0,y0
sol=odeint(rasp,z0,t)

#plt.plot(sol[:,1],sol[:,0],'g',label='y(k)')
plt.plot(sol[:,0],'b',label='x(t)')
plt.plot(sol[:,1],'b',label='y(t)')
plt.legend()

plt.show() 



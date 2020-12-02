import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 

t=np.arange(0,50,0.01)
def rasp(z,t):
    x,v=z
    dxdt=v
    dvdt=-(k*x/m)-0.2*v-g
    return dxdt,dvdt
x0=0.08
v0=0.5
z0=x0,v0
k=1/0.08
g=9.8
m=0.5
sol=odeint(rasp,z0,t)

plt.plot(t,sol[:,0],'b',label='x(t)')
plt.legend()

plt.show() 


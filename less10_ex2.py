
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
x=np.arange(-0.99,0.99,0.0001)
def diff_func(z,x):
    y,k=z
    dy_dx=k
    dk_dx=(x*k-n**2*y)/(1-x**2)
    
    return dy_dx,dk_dx
y0=5
k0=20
n=0.1
z0= y0,k0
sol=odeint(diff_func,z0,x)

#plt.plot(sol[:,1],sol[:,0],'g',label='y(k)')
plt.plot(sol[:,0],'b',label='y(x)')
plt.legend()

plt.show() 


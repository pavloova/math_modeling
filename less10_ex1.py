import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
x=np.arange(0.01,2,0.001)
def diff_func(z,x):
    y,k=z
    dy_dx=k
    dk_dx=((x**2-v**2)*y-x*k)/x**2
    
    return dy_dx,dk_dx
y0=0.5
k0=3
v=1/3
z0= y0,k0
sol=odeint(diff_func,z0,x)

#plt.plot(sol[:,1],sol[:,0],'g',label='y(k)')
plt.plot(sol[:,0],'b',label='y(x)')
plt.legend()


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
t=np.linspace(0,4.5,100)
def velocity(v,t):
    v1=v+f/m*t
    dmdt=f-k*v1**2
    
    return dmdt

m=1
v0=0
f=10
k=0.01
vel=odeint(velocity,v0,t)
plt.plot(t,vel[:,0]) 
plt.legend()
plt.show()




import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
t=np.linspace(0,5,1000)
def bakteria(n,t):
    dmdt=c*n
    return dmdt
n0=1
c=2
n_bac=odeint(bakteria,n0,t)
plt.plot(t,n_bac[:,0],label='Talium') 
plt.legend()
plt.show()

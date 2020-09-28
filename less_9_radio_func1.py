import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 

t = np.arange(0,10**6,100)
def radio_func(m,t):
    dmdt=-k*m
    return  dmdt
m0=10
kUr238= 4.84*10**(-18)
kBi210= 1.61*10**(-6)
kTl210=8.76*10**(-3)
k=kUr238
m_Ur_t=odeint(radio_func,m0,t)

k=kBi210      #function 
m_Bi_t=odeint(radio_func,m0,t)
 
k=kTl210
m_Tl_t=odeint(radio_func,m0,t)

plt.plot(t,m_Ur_t[:,0],label='uran') 
plt.plot(t,m_Bi_t[:,0],label='vismut') 
plt.plot(t,m_Tl_t[:,0],label='Talium') 
plt.legend()
plt.show()
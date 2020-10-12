import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
t=np.linspace(0,365,1000)
def invest_volume(invest,t):
    dinvestdt=-k*invest*t
    return dinvestdt
invest0=1000
k=0.008
vol=odeint(invest_volume,invest0,t)
plt.plot(t,vol[:,0],label='Investments') 
plt.legend()
plt.show()

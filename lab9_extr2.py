
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t=np.linspace(0,10,100)
def velocity(v,t):
    dvdt=(G*m/(R+h)**2)*t
    return dvdt
v0=0
h=20000
G=6.67*10**(-11)
m=5.97*10**24
R=6400000
vel = odeint(velocity, v0, t)

plt.plot(t,vel[:,0],label='velocity')
plt.grid() 
plt.legend()

plt.show()
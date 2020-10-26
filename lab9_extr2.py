
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
h0=200000
r=np.linspace(0,h0,100)
def velocity(v,r):
    dvdt=G*m/(v*(R+h0-r)**2)
    return dvdt
v0=0.01

G=6.67*10**(-11)
m=5.97*10**24
R=6400000
vel = odeint(velocity, v0, r)

plt.plot(r,vel[:,0],label='velocity')
plt.grid() 
plt.legend()

plt.show()

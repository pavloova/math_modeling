import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
# определяем перемеенную величину
t=np.arange(1,10,0.01)

#определяем функцию для системы диффуров
def diff_func(z,t):
    theta,omega= z #указание изменяемых функцийбчерез изменяемую величину системы
    dtheta_dt = omega
    domega_dt=-b*omega- c*np.sin(theta)
    return dtheta_dt,domega_dt #в том же порядке возвращаются
theta0=np.pi-0.1
omega0=0
z0= theta0,omega0
b=0.25
c=5

sol=odeint(diff_func,z0,t)

plt.plot(sol[:,1],sol[:,0],'g',label='theta(omega)')
plt.plot(t,sol[:,0],'b',label='omega(t)')
plt.plot(t,sol[:,1],'r',label='omega(t)')
plt.legend()
plt.axis('equal')
plt.show() 

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots()
circle, = plt.plot([],[],color='b',label='окружность')

def circle_func(alpha,r,x0,y0):
    R=alpha*r
    phi =np.linspace(0,2*np.pi,30)
    x = x0+R*np.cos(phi)
    y= y0+ R*np.sin(phi)
    return x, y
N = 20
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
plt.legend()
plt.axis('equal')
plt.grid()

def animate(i):
    circle.set_data(circle_func(alpha=0.5,r=i,x0=1,y0=1))
ani= FuncAnimation(fig,animate,frames=N,interval=10)
ani.save('circle.gif')



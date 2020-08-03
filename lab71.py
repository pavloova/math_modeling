import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots(figsize=(5,10),facecolor='red ',frameon=True)
circle, = plt.plot([],[],color='b',label='окружность')

def parabola(x0, a, b, c):
    y0 = a * x0**2 + b * x0 + c
    return x0, y0
sub = parabola(x0=np.arange(-1.5,5.5,0.1),a=2,b=-8,c=1)
plt.plot(sub[0],sub[1], label = 'парабола')
def circle_func(R,x0,a,b,c):
    y0=a*x0**2+b*x0+c
    phi =np.linspace(0,2*np.pi,30)
    x = x0+R*np.cos(phi)
    y= y0+ R*np.sin(phi)
    return x, y
N = 20
ax.set_xlim(0,5)
ax.set_ylim(0,8)
plt.legend()
plt.axis('equal')
plt.grid()

def animate(i):
    circle.set_data(circle_func(R=0.3,x0=i,a=2,b=-8,c=1))
ani= FuncAnimation(fig,animate,frames=N,interval=10)
ani.save('parabola.gif')



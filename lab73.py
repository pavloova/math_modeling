import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots(figsize=(10,5))
cycloid, = plt.plot([],[],'g')
point,=plt.plot([],[],'ro')
circle, = plt.plot([],[],color='b',label='окружность')

R=1
def circle_func(R,x0,y0):
    phi =np.linspace(0,4*np.pi,100)
    x =x0+ R*np.cos(phi)
    y= y0+ R*np.sin(phi)
    return x,y

th=np.linspace(0,4*np.pi,100)
x_cycl=R*(th-np.sin(th))
y_cycl=R*(1-np.cos(th))

def animate(i):
    cycloid.set_data(x_cycl[:i+1],y_cycl[:i+1])
    point.set_data(x_cycl[i],y_cycl[i])
    circle.set_data(circle_func(R=1,x0=i,y0=1))

N = 100
ax.set_xlim(0,10)
ax.set_ylim(0,5)
plt.legend()
plt.axis('equal')
plt.grid()


ani= FuncAnimation(fig,animate,interval=50,frames=100)
ani.save('circle.gif')




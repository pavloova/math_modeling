import matplotlib.pyplot as plt
from math import pi
from physicalconstants import e
import numpy as np
k=1
th=np.linspace(0, 8*pi, 10000)
x=k*th*np.cos(th)
y=k*th*np.sin(th)
plt.title('спираль архимедова')
plt.plot(x,y)
plt.axis('equal')
plt.show()



b=5
x= np.sin(b*th)*np.cos(th)
y= np.sin(b*th)*np.sin(th)
plt.title('роза')
plt.plot(x,y)
plt.axis('equal')
plt.show()



c=0.05
x=e**(c*th)*np.cos(th)
y=e**(c*th)*np.sin(th)
plt.title('логарифмическая спиралька')
plt.plot(x,y)
plt.axis('equal')
plt.show()         

a=100
phi=np.linspace(0.01, 4*pi, 10000 )
x=(a/np.sqrt(phi))*np.cos(phi)
y=(a/np.sqrt(phi))*np.sin(phi)
plt.title('спираль жезл')
plt.plot(x,y)
plt.axis('equal')
plt.show()

x=0
y=0
v= 15
j=0
t=0

import numpy as np
a=np.zeros((100,3))
from physicalconstants import g

while t<5:
    t=t+0.1
    j=j+1
    X=x+v*t
    Y=y+v*t-g*(t**2)/2
    a[j,0]=t
    a[j,1]=X
    a[j,2]=Y
print(a)

"""
Spyder Editor

This is a temporary script file.
"""


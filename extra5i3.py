import matplotlib.pyplot as plt
import numpy as np
def function(x1, x2, N, a, b):
    """input ends of a section, number of dots, a,b""" 

    x = np.linspace(x1, x2, N)
    y = np.zeros(N)
    for i in range (N):
        if x[i] < a:
            y[i] = a**2
        elif x[i] >= a and x[i] <= b:
            y[i] = x[i]**2
        else:
            y[i] = b**2
    plt.plot(x,y,label='function')
    plt.xlabel('ось абсцисс')
    plt.ylabel('ось ординат')
    plt.axis('equal')
    plt.show()
function(-50,50,1000,-3,5)

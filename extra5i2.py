def polarellipse(ecc,p):
    import matplotlib.pyplot as plt
    import numpy as np
    from math import pi
    th=np.linspace(0, 8*pi, 10000)
    plt.polar(th,p/(1+ecc*np.cos(th)))
    plt.show()

polarellipse(0.5,2)
def decartellipse (ecc,p):
     import matplotlib.pyplot as plt
     import numpy as np
     from math import pi
     th=np.linspace(0, 8*pi,10000)
     x=p/(1+ecc*np.cos(th))*np.cos(th)
     y=p/(1+ecc*np.cos(th))*np.sin(th)
     plt.plot(x,y,label='ellipse')
     plt.xlabel('ось абсцисс')
     plt.ylabel('ось ординат')
     plt.axis('equal')
     plt.show()
decartellipse(0.5,2)
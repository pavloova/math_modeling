def circle (r,x1,y1):
    import numpy as np
    import matplotlib.pyplot as plt
    x=np.linspace(x1-r,x1+r,1000)
    y=np.linspace(y1-r,y1+r,1000)
    X,Y=np.meshgrid(x,y)
    fxy=(X-x1)**2+(Y-y1)**2 
    plt.contour(X,Y,fxy,levels=[r])
    plt.show()
circle(1,1,1)
def ellipce(x1,y1,a,b,c=10,d=10):
    import numpy as np
    import matplotlib.pyplot as plt
    x=np.linspace(-c,c,1000)
    y=np.linspace(-d,d,1000)
    X,Y=np.meshgrid(x,y)
    fxy=((X-x1)/a)**2 + ((Y-y1)/b)**2
    plt.contour(X,Y,fxy, levels=[1])
    plt.show()
ellipce(1,1,6,4)

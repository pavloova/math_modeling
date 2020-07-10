def parabola (a,b,c,X,X1,n):
    import matplotlib.pyplot as plt
    import numpy as np
    x=np.linspace(X,X1,n)
    y=a*x**2+b*x+c
    plt.plot(x,y,label='парабола')
    plt.xlabel('абцисса')
    plt.ylabel('ордината')

    plt.legend()
    plt.show()
parabola(1,0,0,-4,4,100)
def hyperbola (k,X,X1,n):
    import matplotlib.pyplot as plt
    import numpy as np
    x=np.linspace(X,X1,n)
    y=k/x
    plt.plot(x,y,label='гипербола')
    plt.xlabel('абсцисса')
    plt.ylabel('ордината')

    plt.legend()
    plt.show()
hyperbola(1,1,5,100)
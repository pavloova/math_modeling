def parabola (a,b,c,X,X1,n):
    """введите коэффициенты a,b,c,концы рассматриваемого отрезкаб количество точек"""
    import matplotlib.pyplot as plt
    import numpy as np
    x=np.linspace(X,X1,n)
    y=a*x**2+b*x+c
    plt.plot(x,y,label='парабола')
    plt.xlabel('ось абцисс')
    plt.ylabel('ось ординат')
    plt.axis('equal')
    plt.legend()
    plt.show()
parabola(1,0,0,-4,4,100)
def hyperbola (k,X,X1,n):
    """введите коэффициент к, концы рассматриваемого отрезка, количество точек"""
    import matplotlib.pyplot as plt
    import numpy as np
    x=np.linspace(X,X1,n)
    y=k/x
    plt.plot(x,y,label='гипербола')
    plt.xlabel('ось абсцисс')
    plt.ylabel('ось ординат')
    plt.axis('equal')
    plt.legend()
    plt.show()
hyperbola(1,-5,5,100)

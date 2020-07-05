def func(a,b,n):
    """ this function calculates y=x**2 in certain interval(a<x<b) for several points"""
    import numpy as np
    m=[]
    m=np.linspace(a,b,n)
    
    return (m*m)
y = func(0,4,5)
print(y)
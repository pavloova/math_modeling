def mechenergy(m=0,h=0,v=0): 
    """функция вычисляет полную механическую энергию тела по входным параметрам: масса тела, высота и скорость полета"""
    from physicalconstants import g
    fme=(m*(v**2)/2) + m*h*g
    return(fme)
b = mechenergy(10,10,1)
print(b)


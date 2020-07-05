def mechenergy(m=0,h=0,v=0): 
    """функция вычисляет полную механическую энергию тела по входным параметрам: масса тела, высота и скорость полета"""
    from physicalconstants import g
    full_mech_energy=(m*(v**2)/2) + m*h*g
    return(full_mech_energy)
b = mechenergy(10,10,1)
print(b)


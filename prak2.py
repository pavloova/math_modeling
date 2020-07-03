H=100
v= int()
from physicalconstants import g 
from math import pi,sqrt, tan, cos
a= pi/3
b= pi/6
v= sqrt((g*H*(tan(b))**2)/ (2*(cos(a))**2*(1-tan(b)*tan(a))))
print(v)
T=200 
E=300
from physicalconstants import h,k,e

N=(2/sqrt(pi))*(h/((k*T)**3/2))*(e**(-E/k*T))*(E**(T/2))
print (N)



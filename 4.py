from math import sin
import numpy as np
N= int(input())
M= int(input())
j=0
i=0
k=[]
a=np.ndarray(shape=(N,M))
a[i][j]= sin(N*(i+1)+ M*(j+1))
if a[i][j]<0:
    a[i][j]=0    
print(a)
#k.append (a)
#b=int(input())
#c=int(input())
#k[i][c],k[i][b] =k[i][b],k[i][c]
#print(k)

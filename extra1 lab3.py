N= 2
M= 3
i= 0
j= 0
a=[]
import numpy as np 
a=np.zeros((N,M))
for i in range (N):
    for j in range(M):
        a[i][j]= int(input())

print (a)
b=[]
b=np.zeros((N,M))

for i in range (N):
    for j in range(M):
     
        b[i][j]= int(input())

print (b)
c=[]
c=np.ndarray(shape=(N,M))
c[i,j]=b[i][j]

for i in range (N):
    for j in range(M):
                     if a[i][j]>b[i][j]:
                        c[i][j]=a[i][j]
print(c)
N=10
import numpy as np
def multiply(a):
   
    j=1
    for i in range(N):
       
        j=j*a[i]
    return(j)
a=[]
a = N*[0] 
for i in range(N):
    a[i]=np.array(int(input()))
b= multiply(a)
print(a)
print(b)




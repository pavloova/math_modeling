N=10
import numpy as np
def srednee(a):
   
    j=0
    for i in range(N):
       
        j=j+a[i]
    return(j/N)
a=[]
a = N*[0] 
for i in range(N):
    a[i]=np.array(int(input()))
b= srednee(a)
print(a)
print(b)

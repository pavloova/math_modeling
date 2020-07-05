def square():
    from math import pi
    A=int(input())
    if A==3:
        print('input side length:')
        a= int(input())
        print('input height:')
        h=int(input())
        s = 0.5*a*h
    elif A ==0:
        print('input radius:')
        r= int(input())
        s= pi*(r**2)
    elif A==4:
        print('input length of the side:')
        b= int(input())
        print('input length  another side: ')
        c= int(input())
        s= b*c
    else:
       s = print('i cant help')
    return(s)

print ('which figures square would you like to calculate? input 3 for triangle,0 for circle or 4 for rectangle')
m = square()
print('square= ', m)

def image():
    """This function describes features of the image according to the lens type, focus distance and distance to object"""
    print('please,input the type of the lens.Use "con" for a converging lens and "div" for diverging one')
    a=str(input())
    print('input distance from object to lens')
    d=int(input())
    print('input focus distance')
    F=int(input())
    if a=="con":
        if d<F:
            print ('enlarged, straight, virtual')
        elif d==F:
            print('no image')
        elif F<d<2*F:
            print('enlarged, reverse, real')
        elif d==2*F:
            print('same, reverse, real')
        elif 3*F>d> 2*F:
            print ('diminished, reverse, real')
        else:
            print('a dot in focus, real')
    else:
        if d<F:
            print ('diminished, straight, virtual')
        elif d==F:
            print('diminished,straight, virtual')
        elif F<d<2*F:
            print('diminished,straight, virtual')
        elif d==2*F:
            print('same, straight, virtual')
        elif 3*F>d> 2*F:
            print ('diminished, straight, virtual')
        else:
            print('a dot in focus, virtual')
    return()
l= image()
print (l)


def steps(N):
    import matplotlib.pyplot as plt
    import numpy as np
    import math
    x=np.linspace(0,5,N)
    y=np.zeros(N)
    for i in range (N):
        y[i] = math.floor(x[i])
    plt.title("Лесенка")
    plt.plot(x,y)
    plt.xlabel('ось абсцисс')
    plt.ylabel('ось ординат')
    plt.show()
steps(100)
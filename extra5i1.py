import numpy as np
import matplotlib.pyplot as plt 

def lissajou(b, B=5, A=1, a=1):
    t = np.linspace(0, 100, 1000)
    x =  A * np.sin(a * t + (np.pi/2))
    y = B * np.sin(b * t)
    plt.plot(x, y)
    plt.grid()
    plt.title("Фигура Лиссажу")
    plt.legend()
    
    plt.show()
lissajou(3)


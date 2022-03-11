import numpy as np
import matplotlib.pyplot as plt


x1 = float(input("Unesi x koordinatu 1. tocke: "))
y1 = float(input("Unesi y koordinatu 1. tocke: "))
x2 = float(input("Unesi x koordinatu 2. tocke: "))
y2 = float(input("Unesi y koordinatu 2. tocke: "))

def pravac(x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    l = -k * x1 + y1

    if(l<0):
        print("Jednadzba pravca je: y =",k,"x",l)
    elif(l>0):
        print("Jednadzba pravca je: y =",k,"x +",l)
    else:
        print("Jednadzba pravca je: y =",k,"x")
        
    linije = np.linspace(-5, 5, 50)
    jdb_pravca = k*linije + l
    plt.plot(linije, jdb_pravca)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x1, y1, color = "green", marker = '.', markersize = 6)
    plt.plot(x2, y2, color = "green", marker = '.', markersize = 6)
    plt.show()



pravac(x1, y1, x2,  y2)

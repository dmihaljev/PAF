import numpy as np
import matplotlib.pyplot as plt

tocke = [[]for i in range(2)]
def koordinate(tocke, i):
     x = float(input("Unesi x koordinatu {}. tocke: ".format(i + 1)))
     tocke[i].append(x)
     y = float(input("Unesi y koordinatu {}. tocke: ".format(i + 1)))
     tocke[i].append(y)

def pravac(tocke):
    k = (tocke[1][1] - tocke[0][1]) / (tocke[1][0] - tocke[0][0])
    l = -k * tocke[0][0] + tocke[0][1]

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
    plt.plot(tocke[0][0], tocke[0][1], color = "green", marker = '.', markersize = 6)
    plt.plot(tocke[1][0], tocke[1][1], color = "green", marker = '.', markersize = 6)
    plt.show()


for i in range(2):
    koordinate(tocke, i)
pravac(tocke)

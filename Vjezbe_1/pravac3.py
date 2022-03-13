import numpy as np
import matplotlib.pyplot as plt


def pravac(x1, y1, x2, y2, save = False):
    k = (y2 - y1) / (x2 - x1)
    l = -k * x1 + y1

    if(l<0):
        print("Jednadzba pravca je: y =",k,"x",l)
    elif(l>0):
        print("Jednadzba pravca je: y =",k,"x +",l)
    else:
        print("Jednadzba pravca je: y =",k,"x")
        
    linije = np.linspace(1, 3, 50) # niasm siguran kako staviti neki nacin automatskog odredjivanja intervala koordinatnog sustava za dani pravac pa sam stavio vrijednosti koje odgovaraju tockama pravca
    jdb_pravca = k*linije + l

    plt.plot(linije, jdb_pravca)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x1, y1, color = "green", marker = '.', markersize = 6)
    plt.plot(x2, y2, color = "green", marker = '.', markersize = 6)
    
    if(save):
        plt.savefig("pravac3.pdf") # iz nekog razloga mi nije radila opcija da korisnika pita koje ime zeli, jer kad bih stavio opciju biranja imena u funkciju i pozivao je u glavnom programu, vracalo bi mi pdf.png file iz nekog razloga.
    else:
        plt.show()

x1 = 1
y1 = 2
x2 = 3
y2 = 4

pravac(x1, y1, x2, y2, True)
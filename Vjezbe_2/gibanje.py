import matplotlib.pyplot as plt
import numpy as np
import math

def jednoliko_gibanje(F, m, vrijeme, x0 = 0, v0 = 0):
    t = []
    v = []
    a = []
    x = []

    for i in range(vrijeme):
        dt = 0.1
        t.append(i*dt)
        a.append(F/m) 
        v.append(v0 + a[i]*t[i])
        x.append(x0 + v[i]*t[i])

    plt.plot(t,x)
    plt.xlabel('t[s]')
    plt.ylabel('x[m]')
    plt.title('x-t graf')
    plt.show()

    plt.plot(t,v)
    plt.xlabel('t[s]')
    plt.ylabel('v[m/s]')
    plt.title('v-t graf')
    plt.show()

    plt.plot(t,a)
    plt.xlabel('t[s]')
    plt.ylabel('a[m/s^2]')
    plt.title('a-t graf')
    plt.show()

def kosi_hitac(kut, vrijeme, v0, x0 = 0, y0 = 0):
    t = []
    x = []
    y = []
    vx = []
    vy = []
    ax = []
    ay = []

    g = -9.81
    for i in range(vrijeme):
        t.append(0.1*i)
        ax.append(0)
        ay.append(g)
        vx.append(v0*math.cos(math.radians(kut)) + ax[i]*t[i])
        vy.append(v0*math.sin(math.radians(kut)) + ay[i]*t[i])
        x.append(x0 + vx[i]*t[i])
        y.append(y0 + vy[i]*t[i])

    plt.plot(t,x)
    plt.xlabel('t[s]')
    plt.ylabel('x[m]')
    plt.title('x-t graf')
    plt.show()

    plt.plot(t,y)
    plt.xlabel('t[s]')
    plt.ylabel('y[m]')
    plt.title('y-t graf')
    plt.show()

    plt.plot(x,y)
    plt.xlabel('x[m]')
    plt.ylabel('y[m]')
    plt.title('x-y graf')
    plt.show()

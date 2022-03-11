import matplotlib.pyplot as plt
import numpy as np
import math


def gibanje(F, vrijeme, m, x0 = 0, v0 = 0):
    t = []
    v = []
    a = []
    x = []

    dt = 0.1

    t.append(0.)
    v.append(0.)
    x.append(0.)
    a.append(F/m)

    for i in range(10*vrijeme):
        v.append(v[i] + a[i]*dt)
        x.append(x[i] + v[i]*dt)
        t.append(i*dt)
        a.append(F/m)

    plt.plot(t,x)
    plt.xlabel('t[s]')
    plt.ylabel('x[m]')
    plt.title('x-t graf')
    plt.show()

    plt.plot(v,t)
    plt.xlabel('t[s]')
    plt.ylabel('v[m/s]')
    plt.title('v-t graf')
    plt.show()

    plt.plot(a,t)
    plt.xlabel('t[s]')
    plt.ylabel('a[m/s^2]')
    plt.title('a-t graf')
    plt.show() 

def kosi_hitac(theta, vrijeme, x0=0, y0=0, ):


import math
import numpy as np
import matplotlib.pyplot as plt

class harmonijski_oscilator:
    def __init__(self):
        self.x = []
        self.v = []
        self.a = []
        self.t = []

    def init_cond(self, m, k, x0, v0, dt = 0.01):
        self.m = m
        self.k = k
        self.t.append(0)
        self.x.append(x0)
        self.v.append(v0)
        self.a.append(-(self.k/self.m)*x0)
        self.dt = dt

    def reset (self):
        self.__init__()
    
    def polozaj(self):
        return self.t, self.x
    
    def _move(self, i):
        self.t.append(self.t[i-1] + self.dt)
        self.a.append(-(self.k/self.m)*self.x[i-1])
        self.v.append(self.v[i-1] + self.a[i]*self.dt)
        #print(self.v[i-1], self.a[i])
        self.x.append(self.x[i-1] + self.v[i]*self.dt)

    def oscilacija(self, vrijeme):
        N = int(vrijeme / self.dt)
        for i in range(1, N):
            self._move(i)

    def putanja(self):
        plt.xlabel('t[s]')
        plt.ylabel('x[m]')
        plt.scatter(self.t, self.x, s = 20)
        plt.show()

        plt.xlabel('t[s]')
        plt.ylabel('v[m/s]')
        plt.scatter(self.t, self.v, s = 20)
        plt.show()

        plt.xlabel('t[s]')
        plt.ylabel('a[m/s^2]')
        plt.scatter(self.t, self.a, s = 20)
        plt.show()
import math
import numpy as np
import matplotlib.pyplot as plt

class projectile_drop:
    def __init__(self):
        self.x = []
        self.y = []
        self.h = []
        self.v = []
        self.vx = []
        self.vy = []
        self.ax = []
        self.ay = []
        self.t = []
    def init_cond(self, h0, v0, dt = 0.01):
        self.g = -9.81
        self.t = 0
        self.v.append(v0)
        self.h.append(h0)
        self.ax.append(0)
        self.ay.append(self.g)
        self.dt = dt
    def reset (self):
        self.__init__()
    def ispustanje_projektila(self):
        while self.y[-1] >= 0:
            self.t.append(self.t[-1]+self.dt)
            self.vx.append(self.vx[-1]+self.ax[-1]*self.dt)
            self.vy.append(self.vy[-1]+self.ay[-1]*self.dt)
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
    def vrijeme_trajanja_pada(self):
        while(self.y[len(self.y)-1]>=self.y[0]):
            self.ispustanje_projektila()
        return self.t[len(self.t)-1]
        
    def putanja(self):
        plt.xlabel('x[m]')
        plt.ylabel('y[m]')
        plt.scatter(self.x, self.y)
        plt.show()

        plt.xlabel('vy[m/s]')
        plt.ylabel('t[s]')
        plt.scatter(self.vy, self.t)
        plt.show()
    def ispisivanje(self):
        self.ispustanje_projektila()
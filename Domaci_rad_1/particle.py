import matplotlib.pyplot as plt
import numpy as np
import math

class Particle:
    def __init__(self):
        self.t = []
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.ax = []
        self.ay = []
    def set_init_cond(self, v, kut, x0, y0, dt = 0.001):
        self.g = -9.81
        self.t.append(0)
        self.x.append(x0)
        self.y.append(y0)
        self.vx.append(v*math.cos(math.radians(kut)))
        self.vy.append(v*math.sin(math.radians(kut)))
        self.ax.append(0)
        self.ay.append(self.g)
        self.dt = dt
    def reset (self):
        self.__init__()
    def __move(self):
        self.t.append(self.t[-1] + self.dt)
        self.x.append(self.x[-1] + self.vx[-1]*self.dt)
        self.y.append(self.y[-1] + self.vy[-1]*self.dt)
        self.vx.append(self.vx[-1] + self.ax[-1]*self.dt)
        self.vy.append(self.vy[-1] + self.ay[-1]*self.dt)
        self.ax.append(0)
        self.ay.append(self.g)
    def range(self):
        while self.y[-1]>=0:
            self.__move()
            #print(self.y[-1])
        return self.x[-1]

    def total_time(self):
        while self.y[-1]>=0:
            self.__move()
        return self.t[-1]

    def max_speed(self):
        for i in range(0, int(self.t[-1])): #Racunao sam da se trazi maksimalna horizontalna brzina, ako je to to, jer pocetna brzina bi trebala bit najveca postignuta brzina tijela, s obzirom da nema otpora zraka
            self.__move()
        return self.vx[-1]

    def putanja(self):
        plt.plot(self.x, self.y)
        plt.xlabel('x[m]')
        plt.ylabel('y[m]')
        plt.show()

        #FGraf ovisnosti vremena o dometu
        plt.plot(self.t, self.x)
        plt.xlabel('x[m]')
        plt.ylabel('t[s]')
        plt.show()
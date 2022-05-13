import matplotlib.pyplot as plt
import numpy as np
import math
g = -9.81
ro = 1.5
class Projectile:
    def __init__(self):
        self.t = []
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.ax = []
        self.ay = []
        self.dt = []
        self.ro = ro

    def set_init_cond(self, v, kut, masa, otpor, povrsina, dt = 0.001):
        self.g = -9.81
        self.t.append(0)
        self.x.append(0)
        self.y.append(0)
        self.vx.append(v*math.cos(math.radians(kut)))
        self.vy.append(v*math.sin(math.radians(kut)))
        self.ax.append(0)
        self.ay.append(self.g)
        self.m = masa
        self.Cd = otpor
        self.A = povrsina
        self.dt = dt
    def reset (self):
        self.__init__()
    def __move(self):
        self.t.append(self.t[-1] + self.dt)
        self.x.append(self.x[-1] + self.vx[-1]*self.dt)
        self.y.append(self.y[-1] + self.vy[-1]*self.dt)
        self.vx.append(self.vx[-1] + self.ax[-1]*self.dt)
        self.vy.append(self.vy[-1] + self.ay[-1]*self.dt)
        self.ax.append(-1*np.sign(self.vx[-1])*((self.ro*self.Cd*self.A)/(2*self.m))*self.vx[-1]**2)
        self.ay.append(self.g-1*np.sign(self.vy[-1])*((self.ro*self.Cd*self.A)/(2*self.m))*self.vy[-1]**2)
    def _a(self, x, v, t):
        return -1*np.sign(v)*((self.ro*self.Cd*self.A)/(2*self.m))*v**2
    def _move_rk(self):
        self.t.append(self.t[-1] + self.dt)

        k1vx = (self._a(self.x[-1], self.vx[-1], self.t[-1]))*self.dt
        k1vy = (self.g + self._a(self.y[-1], self.vy[-1], self.t[-1]))*self.dt
        k1x = self.vx[-1] * self.dt
        k1y = self.vy[-1] * self.dt

        k2vx = (self._a(self.x[-1]+k1x/2, self.vx[-1]+k1vx/2, self.t[-1]+self.dt/2))*self.dt
        k2vy = (self.g + self._a(self.y[-1]+k1y/2, self.vy[-1]+k1vy/2, self.t[-1]+self.dt/2))*self.dt
        k2x = (self.vx[-1]+k1vx/2) * self.dt
        k2y = (self.vy[-1]+k1vy/2) * self.dt

        k3vx = (self._a(self.x[-1]+k2x/2, self.vx[-1]+k2vx/2, self.t[-1]+self.dt/2))*self.dt
        k3vy = (self.g + self._a(self.y[-1]+k2y/2, self.vy[-1]+k2vy/2, self.t[-1]+self.dt/2))*self.dt
        k3x = (self.vx[-1]+k2vx/2) * self.dt
        k3y = (self.vy[-1]+k2vy/2) * self.dt

        k4vx = (self._a(self.x[-1]+k3x/2, self.vx[-1]+k3vx/2, self.t[-1]+self.dt/2))*self.dt
        k4vy = (self.g + self._a(self.y[-1]+k3y/2, self.vy[-1]+k3vy/2, self.t[-1]+self.dt/2))*self.dt
        k4x = (self.vx[-1]+k3vx/2) * self.dt
        k4y = (self.vy[-1]+k3vy/2) * self.dt

        self.vx.append(self.vx[-1] + (k1vx + 2*k2vx + 2*k3vx + k4vx)/6)
        self.vy.append(self.vy[-1] + (k1vy + 2*k2vy + 2*k3vy + k4vy)/6)
        self.x.append(self.x[-1] + (k1x + 2*k2x + 2*k3x + k4x)/6)
        self.y.append(self.y[-1] + (k1y + 2*k2y + 2*k3y + k4y)/6)

    def putanja(self):
        while self.y[-1] >= 0:
            self.__move()
        return self.x, self.y

    def putanja_rk(self):
        while self.y[-1] >= 0:
            self._move_rk()
        return self.x, self.y

    def domet(self):
        self.putanja_rk()
        return self.x[-1]
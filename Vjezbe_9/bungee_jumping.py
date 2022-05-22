import numpy as np
import math

g = -9.81
ro = 1.2
class BungeeJumping:

    def __init__(self):
        self.t = []
        self.y = []
        self.v = []
        self.a = []
        self.E_el = []
        self.Ek = []
        self.Ep = []
        self.E_uk = []

    def init_cond(self, masa, h, l, otpor, povrsina, k, dt = 0.01):
        self.t.append(0)
        self.y.append(h)
        self.v.append(0)
        self.a.append(g)
        self.m = masa
        self.h = h
        self.l = l
        self.Cd = otpor
        self.A = povrsina
        self.k = k
        self.dt = dt
        self.g = g
        self.ro = ro
        self.energija(h, 0)
    def reset (self):
        self.__init__()
    def _a(self, y, v, t):
        if(y + self.l > self.h):
            dy = 0.
        else:
            dy = (y+self.l)-self.h
        return self.g -self.k*dy/self.m-1*np.sign(v)*((self.ro*self.Cd*self.A)/(2*self.m))*v**2

    def energija(self, y, v):
        Ek = 0.5*self.m*v**2
        Ep = self.m*self.g*y
        if(y + self.l > self.h):
            dy = 0.
        else:
            dy = (y+self.l)-self.h
        E_el = 0.5*self.k*dy**2
        self.Ek.append(Ek)
        self.Ep.append(Ep)
        self.E_el.append(E_el)
        self.E_uk.append(Ek + Ep + E_el)

    def _move_rk(self, i):
        self.t.append(self.t[i-1] + self.dt)

        k1v = (self._a(self.y[i-1], self.v[i-1], self.t[i-1]))*self.dt
        k1y = self.v[-1] * self.dt

        k2v = (self._a(self.y[i-1]+k1y/2, self.v[i-1]+k1v/2, self.t[i-1]+self.dt/2))*self.dt
        k2y = (self.v[i-1]+k1v/2) * self.dt

        k3v = (self._a(self.y[i-1]+k2y/2, self.v[i-1]+k2v/2, self.t[i-1]+self.dt/2))*self.dt
        k3y = (self.v[i-1]+k2v/2) * self.dt

        k4v = (self._a(self.y[i-1]+k3y/2, self.v[i-1]+k3v/2, self.t[i-1]+self.dt/2))*self.dt
        k4y = (self.v[i-1]+k3v/2) * self.dt

        self.v.append(self.v[i-1] + (k1v + 2*k2v + 2*k3v + k4v)/6)
        self.y.append(self.y[i-1] + (k1y + 2*k2y + 2*k3y + k4y)/6)

        self.energija(self.y[i], self.v[i])

    def pomak(self, vrijeme):
        vrijeme = 30
        i = 0
        while self.t[i] < vrijeme and self.y[i]>0 :
            self._move_rk(i)
            i +=1
        return self.t, self.y

    def doseg_energije(self):
        return self.Ek, self.Ep, self.E_el, self.E_uk


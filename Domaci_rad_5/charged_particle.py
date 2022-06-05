import math
import numpy as np
import matplotlib.pyplot as plt

class chargedparticle:
    def __init__(self, q, m, v, E, B, dt=0.01):
        self.a = np.array([0.,0.,0.])
        self.x = []
        self.y = []
        self.z = []
        self.t = []

        self.E = E
        self.B = B

        self.q = q
        self.m = m
        self.v = v

        self.dt = dt

    def _move(self, i):
        self.t.append(self.t[i-1] + self.dt)
        self.a = (self.q/self.m)*(self.E(self.t) + np.cross([self.v, self.B(self.t)]))
        self.v += self.a*self.dt

        self.x.append(self.x[i-1] + self.v[0]*self.dt)
        self.y.append(self.y[i-1] + self.v[1]*self.dt)
        self.z.append(self.z[i-1] + self.v[2]*self.dt)

    def _move_rk(self, i):
        self.t.append(self.t[i-1] + self.dt)

        k1v = (self.q/self.m)*(self.E(self.t) + np.cross([self.v,self.B(self.t)]))*self.dt
        k1r = self.v*self.dt

        k2v = (self.q/self.m)*(self.E(self.t) + np.cross([self.v + k1v/2,self.B(self.t)]))*self.dt
        k2r = (self.v + k1v/2)*self.dt

        k3v = (self.q/self.m)*(self.E(self.t) + np.cross([self.v + k2v/2,self.B(self.t)]))*self.dt
        k3r = (self.v + k2v/2)*self.dt

        k4v = (self.q/self.m)*(self.E(self.t) + np.cross([self.v + k3v/2,self.B(self.t)]))*self.dt
        k4r = (self.v + k2v/2)*self.dt

        self.v += (k1v + 2*k2v + 2*k3v + k4v)/6
        self.x.append(self.x[i-1] + (k1r[0] + 2*k2r[0] + 2*k3r[0] + k4r[0])/6)
        self.y.append(self.y[i-1] + (k1r[1] + 2*k2r[1] + 2*k3r[1] + k4r[1])/6)
        self.z.append(self.z[i-1] + (k1r[2] + 2*k2r[2] + 2*k3r[2] + k4r[2])/6)
    def trajektorija(self, vrijeme, metoda = 'Euler'):
        self.t.append(0)
        self.x.append(0)
        self.y.append(0)
        self.z.append(0)

        N = int(vrijeme/self.dt)
        for i in range(1, N):
            if(metoda == 'rk'):
                self._move_rk(i)
            else:
                self._move(i)
        return self.x, self.y, self.z

    
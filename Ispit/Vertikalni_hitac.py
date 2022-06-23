import numpy as np
import matplotlib.pyplot as plt
import math

class VertikalniHitac():
    def __init__(self, h, v):
        self.h0 = h
        self.v0 = v
        print('Objekt uspješno stvoren. Pocetna visina objekta je:', self.h0, 'm, a pocetna brzina objekta je:', self.v0, 'm/s.')

    def promijeni_visinu(self, h_new):
        self.h0 = h_new
        return self.h0

    def promijeni_brzinu(self, v_nova):
        self.v0 = v_nova
        return self.v0

    def numericki_ve_hitac(self, dt=0.01, i = 0):
        self.x = [0]
        self.a_x = i
        self.vx = [self.a_x]
        self.h = [self.h0]
        self.vy = [0]
        self.t = [0]
        g = 9.81

        while self.h[-1]>0:
            self.x.append(self.x[-1]+self.vx[-1]*dt)
            self.t.append(self.t[-1] + dt)
            self.vy.append(self.vy[-1]+dt*g)
            self.h.append(self.h[-1]-self.vy[-1]*dt)
            self.vx.append(self.vx[-1]+self.a_x*dt)

        return self.h, self.t, self.vy

    def vrijeme_pada_objekta(self, dt=0.01):
        self.numericki_ve_hitac(dt)
        return self.t[-1]
        
    

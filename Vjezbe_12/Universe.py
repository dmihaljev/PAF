import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Planets:
    def __init__(self, ime_planeta, color, m, r, v):
        self.ime_planeta = ime_planeta
        self.color = color
        self.m = m
        self.r = r
        self.v = v
        self.a = np.array((0.,0.))

        self.x = []
        self.y = []
        self.dr = [] # za racunanje udaljenosti svih planeta za racunanje sile
        self.x.append(r[0])
        self.y.append(r[1])

class universe:
    G = 6.67428e-11
    dan = 60*60*24
    def __init__(self, dt = 0.1):
        self.planeti = []
        self.t = []
        self.dt = dt * self.dan #pomak
    def dodaj_planet(self, planet):
        self.planeti.append(planet)
    def putanja(self, vrijeme, metoda = 'Euler'):
        self.t.append(0)
        N = int(vrijeme/self.dt)
        for i in range(1, N):
                self._move(i)
    def _move(self, i):
        self.t.append(self.t[i-1] + self.dt)
        for p1 in self.planeti: # racunamo udaljenost p1 u odnosu na druge planete
            p1.dr.clear() 
            for p2 in self.planeti: # racunamo udaljenost p2 u odnosu na druge planete
                if (p1 == p2):
                    p1.dr.append(np.array((0.,0.))) # ako se putanja jednog planeta poklapa sa drugom, doprinos sila je 0
                else:
                    p1.dr.append((-1*self.G*p2.m*(p1.r - p2.r))/(np.linalg.norm(p1.r - p2.r))**3) # ako se ne poklapaju, u obzir dolazi newton-ov zakon gravitacije
           
            p1.a *= 0
            for dr in p1.dr:
                p1.a += dr # zbroj doprinosa svih planeta u ukupnoj akceleraciji
            p1.v += p1.a*self.dt # dodaje novi doprinos brzine preko euler-ove metode
            p1.r += p1.v*self.dt # dodaje novi doprinos polozaja preko euler-ove metode

            p1.x.append(p1.r[0])
            p1.y.append(p1.r[1])
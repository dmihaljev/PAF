import matplotlib.pyplot as plt

class gibanje:
    def __init__(self):
        self.t = []
        self.m = []
        self.x = []
        self.v = []
        self.a = []
    def init_cond(self,f,m0,x0,v0,dt=0.01):
        self.f = f
        self.t = [0]
        self.x.append(x0)
        self.v.append(v0)
        self.m.append(m0)
        self.a.append(self.f(self.v[-1], self.x[-1],self.t[-1])/self.m[-1])
        self.dt = dt
    def _move(self):
         for i in range(500):
            self.t.append(self.t[-1]+self.dt)
            self.v.append(self.v[-1]+self.a[-1]*self.dt)
            self.x.append(self.x[-1]+self.v[-1]*self.dt)
            self.a.append(self.f(self.v[-1], self.x[-1],self.t[-1])/self.m[-1])
    def putanja(self):
        plt.xlabel('t[s]')
        plt.ylabel('x[m]')
        plt.scatter(self.t, self.x)
        plt.show()

        plt.xlabel('t[s]')
        plt.ylabel('v[m/s]')
        plt.scatter(self.t, self.v)
        plt.show()

        plt.xlabel('t[s]')
        plt.ylabel('a[m/s^2]')
        plt.scatter(self.t, self.a)
        plt.show()
            
    def ispisivanje(self):
        self._move()
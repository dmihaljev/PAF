import harmonijski_oscilator as h
import numpy as np
import matplotlib.pyplot as plt
import math

h1 = h.harmonijski_oscilator()
h1.init_cond(0.2,8,0.5,0,0.1)
h1.oscilacija(3)
h1.putanja()

t1 = []
x1 = []
t1, x1 = h1.polozaj()
h1.init_cond(0.2,8,0.5,0,0.1)
h1.oscilacija(3)
plt.scatter(t1,x1, s = 5, c = 'red')

t2 = []
x2 = []
h1.reset()
h1.init_cond(0.2,8,0.5,0,0.01)
t2, x2 = h1.polozaj()
h1.oscilacija(3)
plt.scatter(t2,x2, s = 5, c = 'green')

t3 = []
x3 = []
h1.reset()
h1.init_cond(0.2,8,0.5,0,0.05)
t3, x3 = h1.polozaj()
h1.oscilacija(3)
plt.scatter(t3,x3, s = 5, c = 'blue')

ta = np.arange(0,3,0.01)
fi = np.pi/4
omega = np.sqrt(5/0.1)
xa = 0.5*np.sin(omega*ta+fi)
plt.scatter(ta,xa, s = 5, c='black')

plt.xlabel('t[s]')
plt.ylabel('x[m]')

plt.show()
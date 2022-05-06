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
h2 = h.harmonijski_oscilator()
t1, x1 = h2.polozaj()
h2.init_cond(0.2,8,0.5,0,0.1)
h2.oscilacija(3)
plt.scatter(t1,x1, s = 5, c = 'red')

t2 = []
x2 = []
h3 = h.harmonijski_oscilator()
h3.reset()
h3.init_cond(0.2,8,0.5,0,0.01)
t2, x2 = h3.polozaj()
h3.oscilacija(3)
plt.scatter(t2,x2, s = 5, c = 'green')

t3 = []
x3 = []
h4 = h.harmonijski_oscilator()
h4.reset()
h4.init_cond(0.2,8,0.5,0,0.05)
t3, x3 = h4.polozaj()
h4.oscilacija(3)
plt.scatter(t3,x3, s = 5, c = 'blue')

ta = np.arange(0,3,0.01)
fi = np.pi/4
omega = np.sqrt(5/0.1)
xa = 0.5*np.sin(omega*ta+fi)
plt.scatter(ta,xa, s = 5, c='black')

plt.xlabel('t[s]')
plt.ylabel('x[m]')

plt.show()

ana_period = 2*math.pi*math.sqrt(0.2/8)
print(ana_period)

h2.num_period()
h3.num_period()
h4.num_period()
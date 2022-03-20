import matplotlib.pyplot as plt
import numpy as np
import math

g = -9.81
v0 = 20
kut = 60

t = []
x = []
y = []
vx = []
vy = []
ax = []
ay = []

for i in range(100):
    t.append(0.1*i)
    ax.append(0)
    ay.append(g)
    vx.append(v0*math.cos(math.radians(kut)) + ax[i]*t[i])
    vy.append(v0*math.sin(math.radians(kut)) + ay[i]*t[i])
    x.append(vx[i]*t[i])
    y.append(vy[i]*t[i])

plt.plot(t,x)
plt.xlabel('t[s]')
plt.ylabel('x[m]')
plt.show()

plt.plot(t,y)
plt.xlabel('t[s]')
plt.ylabel('y[m]')
plt.show()

plt.plot(x,y)
plt.xlabel('x[m]')
plt.ylabel('y[m]')
plt.show()

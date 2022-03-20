import matplotlib.pyplot as plt
import numpy as np

t = []
v = []
a = []
x = []

m = 1.5
F = 15
dt = 0.1

t.append(0.)
v.append(0.)
x.append(0.)
a.append(F/m)
for i in range(100):
    v.append(v[i] + a[i]*dt)
    x.append(x[i] + v[i]*dt)
    t.append(i*dt)
    a.append(F/m)

plt.plot(t,x)
plt.xlabel('t[s]')
plt.ylabel('x[m]')
plt.title('x-t graf')
plt.show()

plt.plot(t,v)
plt.xlabel('t[s]')
plt.ylabel('v[m/s]')
plt.title('v-t graf')
plt.show()

plt.plot(t,a)
plt.xlabel('t[s]')
plt.ylabel('a[m/s^2]')
plt.title('a-t graf')
plt.show()
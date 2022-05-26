import numpy as np
import nabijena_cestica as nc
import matplotlib.pyplot as plt

B = np.array((0,0,1))
E = np.array((0,0,0))

q_el = -1
q_po = 1
m_el = 1
m_po = 1
v_el = np.array((0.1,0.1,0.1))
v_po = np.array((0.1,0.1,0.1))

elektron = nc.NabijenaCestica(q_el,m_el,v_el,E,B,0.01)
pozitron = nc.NabijenaCestica(q_po,m_po,v_po,E,B,0.01)
x_el, y_el, z_el = elektron.trajektorija(30,'rk')
x_po, y_po, z_po = pozitron.trajektorija(30,'rk')

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

ax.plot3D(x_el, y_el, z_el, c = "black")
ax.plot3D(x_po, y_po, z_po, c = "brown")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()


q_eu= -1
q_rk = -1
m_eu = 1
m_rk = 1
v_eu = np.array((0.1,0.1,0.1))
v_rk = np.array((0.1,0.1,0.1))

euler = nc.NabijenaCestica(q_eu,m_eu,v_eu,E,B,0.01)
rk = nc.NabijenaCestica(q_rk,m_rk,v_rk,E,B,0.01)
x_eu, y_eu, z_eu = euler.trajektorija(30,'euler')
x_rk, y_rk, z_rk = rk.trajektorija(30,'rk')

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

ax.plot3D(x_eu, y_eu, z_eu, c = "black")
ax.plot3D(x_rk, y_rk, z_rk, c  = "brown")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
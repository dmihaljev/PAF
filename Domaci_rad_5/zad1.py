import numpy as np
import charged_particle as cp
import matplotlib.pyplot as plt

B = np.array([0,0,1])
E = np.array([0,0,0])

def B1(t):
    B1 = np.array([0,0,t/10])
    return B1

def E1(t):
    E1 = np.array([0,0,t/10])
    return E1

q_el = -1
q_po = 1
m_el = 1
m_po = 1
v_el = np.array((0.1,0.1,0.1))
v_po = np.array((0.1,0.1,0.1))

elektron = cp.chargedparticle(q_el,m_el,v_el,E,B,0.01)
x_el, y_el, z_el = elektron.trajektorija(10,'rk')

elektron_pr = cp.chargedparticle(q_el,m_el,v_el,E1,B1,0.01)
x_el_pr, y_el_pr, z_el_pr = elektron_pr.trajektorija(10,'rk')

pozitron_pr = cp.chargedparticle(q_po,m_po,v_po,E1,B1,0.01)
x_po_pr, y_po_pr, z_po_pr = pozitron_pr.trajektorija(10,'rk')

fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')

#elektron u konstantnom i promjenjivom magnetnom polju
ax.plot3D(x_el, y_el, z_el, c = "black", label = "konstantno")
ax.plot3D(x_el_pr, y_el_pr, z_el_pr, c = "brown", label = "promjenjivo")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

#elektron i pozitron u promjenjivom magnetnom polju
ax.plot3D(x_el_pr, y_el_pr, z_el_pr, c = "black", label = "promjenjivo")
ax.plot3D(x_po_pr, y_po_pr, z_po_pr, c = "brown", label = "promjenjivo")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

# ne znam rijesiti " 'numpy.ndarray' object is not callable" problem.
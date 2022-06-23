import matplotlib.pyplot as plt

from Vertikalni_hitac import VertikalniHitac

objekt = VertikalniHitac(10, 10)

h, v, t = objekt.numericki_ve_hitac()

plt.plot(t, h)
plt.title('Ovisnost visine objekta h o vremenu t')
plt.xlabel('t [s]')
plt.ylabel('h [m]')
plt.show()

plt.plot(t, v)
plt.title('Ovisnost brzine objekta o vremenu')
plt.xlabel('v [m/s]')
plt.ylabel('t [s]')
plt.show()
import Universe
import numpy as np
import matplotlib.pyplot as plt

au = 1.496e11
dan = 60*60*24
godina = 365.242*dan

sun = Universe.Planets("Sun", "yellow", 1.989e30, np.array((0.,0.)), np.array((0.,0.)))
mercury = Universe.Planets("Mercury","orange", 3.285e23, np.array((0., 0.466*au)), np.array((-47362., 0.)))
venus = Universe.Planets("Venus","red", 4.867e24, np.array((-0.723*au,0.)), np.array((0.,35020.)))
earth = Universe.Planets("Earth","blue", 5.9742e24, np.array((-1*au,0.)), np.array((0.,29783.)))
mars = Universe.Planets("Mars","brown", 6.38e24, np.array((0., -1.52*au)), np.array((24007., 0.)))

ss = Universe.universe()
ss.dodaj_planet(sun)
ss.dodaj_planet(mercury)
ss.dodaj_planet(venus)
ss.dodaj_planet(earth)
ss.dodaj_planet(mars)

ss.putanja(5*godina)

fig= plt.figure(figsize=(10,10))
plt.plot(sun.x,sun.y,label=sun.ime_planeta,color=sun.color, linewidth=5.0)
plt.plot(mercury.x,mercury.y,label=mercury.ime_planeta,color=mercury.color)
plt.plot(mercury.x[-1], mercury.y[-1], 'o', color=mercury.color)
plt.plot(venus.x,venus.y,label=venus.ime_planeta,color=venus.color)
plt.plot(venus.x[-1], venus.y[-1], 'o', color=venus.color)
plt.plot(earth.x,earth.y,label=earth.ime_planeta,color=earth.color)
plt.plot(earth.x[-1], earth.y[-1], 'o', color=earth.color)
plt.plot(mars.x,mars.y,label=mars.ime_planeta,color=mars.color)
plt.plot(mars.x[-1], mars.y[-1], 'o', color=mars.color)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Planeti graf')
plt.legend(loc="upper right")
plt.show()


import svemir
import numpy as np
import matplotlib.pyplot as plt

au = 1.496e11
dan = 60*60*24
godina = 365.242*dan

sun = svemir.Planeti("Sun", 1.989e30, np.array((0.,0.)), np.array((0.,0.)))
earth = svemir.Planeti("Earth", 5.9742e24, np.array((-1*au,0.)), np.array((0.,29783.)))

ss = svemir.Svemir()
ss.dodaj_planet(sun)
ss.dodaj_planet(earth)

ss.putanja(1.0*godina)

fig= plt.figure(figsize=(10,10))
plt.plot(sun.x,sun.y,label=sun.ime_planeta,color="yellow", linewidth=5.0)
plt.plot(earth.x,earth.y,label=earth.ime_planeta,color="blue")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Sunce - Zemlja graf')
plt.legend(loc="upper right")
plt.show()
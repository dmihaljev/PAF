import Projectile_drop as pd
import visina_brzina as vb
import matplotlib.pyplot as plt
import numpy as np

p0 = pd.projectile_drop()
p1 = vb.projectile_drop()
p0.init_cond(10, 20)
print("Objekt je uspjesno stvoren")
print("Pocetna brzina je v = {} m/s i pocetna visina je {} m".format(10, 20))

p1 = vb.projectile_drop()
print(p1.unos_v_h)

p2 = pd.projectile_drop()
p2.init_cond(2000, 200, 0.01)
p2.ispisivanje()
p2.putanja()

p3 = pd.projectile_drop()
p1.init_cond(2000, 200)
p3.vrijeme_trajanja_pada()
x_os = np.linspace(0.001,0.1,100)
y_os = p3.vrijeme_trajanja_pada*x_os
plt.plot(x_os, y_os)

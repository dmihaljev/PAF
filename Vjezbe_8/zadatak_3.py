import projectile as pr
import numpy as np
import matplotlib.pyplot as plt

p1 = pr.Projectile()
domet_mase = []
m1 = np.arange(0.5, 5, 50)

for masa in m1:
    p1.set_init_cond(20,60,masa,0.3,0.05,0.01)
    domet_mase += p1.domet()

plt.plot(m1,domet_mase,label="dt=0.01")
plt.xlabel('m1[kg]')
plt.ylabel('domet_mase[m]')
plt.show()


p2 = pr.Projectile()
domet_otpora = []
Cd1 = np.arange(0.5, 5, 50)

for Cd in Cd1:
    p2.set_init_cond(20,60,0.1,Cd,0.05,0.01)
    domet_otpora += p2.domet()

plt.plot(Cd1, domet_otpora,label="dt=0.01")
plt.xlabel('Cd1')
plt.ylabel('domet_otpora[m]')
plt.show()


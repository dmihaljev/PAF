import particle as prt
import numpy as np
import matplotlib.pyplot as plt

p1 = prt.Particle()

p1.set_init_cond(10, 60, 0, 0)
print("Za brzinu v = {} m/s i kut od {} stupnjeva, domet je {} m".format(10, 60, p1.range()))
p1.putanja()
p1.reset()

greska = []
vrijeme  = []
analiticko_rjesenje = 8.835

for i in np.arange(0.0001, 0.1, 0.0001):
    p1.set_init_cond(10,60,0,0,i)
    greska.append(100*(abs(p1.range()-analiticko_rjesenje)/analiticko_rjesenje))
    vrijeme.append(i)

vrijeme.reverse()
plt.plot(vrijeme,greska)
plt.xlabel('vrijeme[s]')
plt.ylabel('apsolutna greska[%]')
plt.show()
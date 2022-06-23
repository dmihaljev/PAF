import matplotlib.pyplot as plt
import numpy as np
from Vertikalni_hitac import VertikalniHitac

objekt = VertikalniHitac(10, 10)

print('Vrijeme trajanja pada objekta je:',objekt.vrijeme_pada_objekta(0.01))
print('Maksimalna visina objekta je:',objekt.maksimalna_visina(0.01))
korak = np.arange(0.0001, 0.1, 0.0001)
trajanje_pada = []

for dt in korak:
    trajanje_pada.append(objekt.vrijeme_pada_objekta(dt))

plt.plot(korak, trajanje_pada)
plt.title('Ovisnost vremena trajanja pada o koraku delta_t')
plt.xlabel('dt [s]')
plt.ylabel('vrijeme trajanja pada t [s]')
plt.show()
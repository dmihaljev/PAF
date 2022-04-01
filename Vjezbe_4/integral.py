from numbers import Integral
import calculus as cal
import numpy as np
import matplotlib.pyplot as plt

def funkcija(x):
    return x*x + 1
     

analiticko_rjesenje = 4/3

gornja_medja, donja_medja = cal.integral_gornja_donja(funkcija, 1, 0, 10)

gornja = []
donja = []
trapezna_metoda = []
broj_koraka = []

for i in np.arange(40, 1000, 40):
    broj_koraka.append(i)
    gornja_medja, donja_medja = cal.integral_gornja_donja(funkcija, 1, 0, i)
    trapezna_metoda.append(cal.integracija(funkcija, 1, 0, i))
    donja.append(donja_medja)
    gornja.append(gornja_medja)

plt.scatter(broj_koraka, gornja, c = 'r')
plt.scatter(broj_koraka, donja, c = 'g')
plt.scatter(broj_koraka, trapezna_metoda, c = 'b')

plt.axhline(analiticko_rjesenje)

plt.xlabel('Broj koraka')
plt.ylabel('Integral')

plt.show()
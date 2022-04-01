import calculus as cal
import numpy as np
import matplotlib.pyplot as plt

def funkcija(x):
    return 2*x*x*x + 3*x*x + 4*x + 5
print(cal.value(funkcija, 0))
print(cal.derivacija_u_tocki(funkcija, 0))

x_os = np.linspace(-3.4,2.4,100)
y_os = 6*x_os*x_os + 6*x_os + 4*x_os
plt.plot(x_os, y_os)

x, dfx = cal.derivacija_u_rasponu(funkcija, -3.4,2.4,0.1, metoda = 1)

x, dfx = cal.derivacija_u_rasponu(funkcija,-3.4,2.4,0.01, metoda = 1)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.scatter(x, dfx, s = 5, color = 'r', marker = 5)
plt.show()

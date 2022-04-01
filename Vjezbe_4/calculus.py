import math
import numpy as np

def value(funkcija, x):
    return funkcija(x)

def derivacija_u_tocki(funkcija, x, h = 0.1, metoda = 2):
    if metoda == 1:
        return (funkcija(x+h) - funkcija(x))/h
    elif metoda == 2:
        return (funkcija(x+h) - funkcija(x-h))/(2*h)
    else:
        return (funkcija(x) - funkcija(x-h)/h)

def derivacija_u_rasponu(funkcija, a, b, h = 0.1, metoda = 2):
    x = []
    dfx = []

    for i in np.arange(a, b, h):
        x.append(i)
        dfx.append(derivacija_u_tocki(funkcija, i, h, metoda))
    return x, dfx

def integral_gornja_donja(funkcija, gornja, donja, N):
    suma_gornja = 0.
    suma_donja = 0.
    dN = (gornja - donja) / N
    for i in range(0, N):
        suma_donja  = suma_donja + funkcija(i*dN)*dN
        suma_gornja = suma_gornja + funkcija((i+1)*dN)*dN
    return suma_donja, suma_gornja

def integracija(funkcija, gornja, donja, N):
    suma = 0.
    dN = (gornja - donja) / N
    
    for i in range(0, N):
        suma = suma + funkcija(i*dN) + funkcija((i+1)*dN)
    return (suma*dN)/2
import gibanje as g0
import numpy as np
import matplotlib.pyplot as plt

def fconst(v,x,t):
    sila = 15
    return 15

def f_opruge(v,x,t):
    k = 10
    return -k*x
    
g1 = g0.gibanje()
g1.init_cond(fconst,2,0,2,0.01)
g1.ispisivanje()
g1.putanja()

g2 = g0.gibanje()
g2.init_cond(f_opruge,2,0,2,0.01)
g2.ispisivanje()
g2.putanja()
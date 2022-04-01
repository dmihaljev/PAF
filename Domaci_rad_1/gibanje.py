import particle as prt
import numpy as np
import matplotlib.pyplot as plt

p1 = prt.Particle()

p1.set_init_cond(10, 60, 0, 0)
print("Za brzinu v = {} m/s i kut od {} stupnjeva, domet je {} m".format(10, 60, p1.range()))
print("Ukupno vrijeme za brzinu v = {} m/s i kut od {} stupnjeva je {}".format(10, 60, p1.total_time()))
print("Maksimalna postignuta brzina projektila je {} m/s".format(p1.max_speed()))
p1.putanja()
p1.reset()
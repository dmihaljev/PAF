import Universe
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

au = 1.496e11
dan = 60*60*24
godina = 365.242*dan

sun = Universe.Planets("Sun", "yellow", 1.989e30, np.array((0.,0.)), np.array((0.,0.)))
mercury = Universe.Planets("Mercury","orange", 3.285e23, np.array((0., 0.466*au)), np.array((-47362., 0.)))
venus = Universe.Planets("Venus","red", 4.867e24, np.array((-0.723*au,0.)), np.array((0.,35020.)))
earth = Universe.Planets("Earth","blue", 5.9742e24, np.array((-1*au,0.)), np.array((0.,29783.)))
mars = Universe.Planets("Mars","brown", 6.38e24, np.array((0., -1.52*au)), np.array((24007., 0.)))

ss = Universe.universe()
ss.dodaj_planet(sun)
ss.dodaj_planet(mercury)
ss.dodaj_planet(venus)
ss.dodaj_planet(earth)
ss.dodaj_planet(mars)

ss.putanja(5*godina)

xs, ys, xm, ym, xv, yv, xe, ye, xm1, ym1 = [], [], [], [], [], [], [], [], [], [] # liste za plotanje planeta
fig = plt.figure(figsize=[10, 10])
plt.rcParams["figure.autolayout"] = True
axes = fig.add_subplot(1,1,1)
ax = plt.axes(xlim=(-2.5e11, 2.5e11), ylim=(-2.5e11, 2.5e11))
line, = ax.plot([], lw = 2)
ax.set_aspect('auto')
ax.axis('off')


linesun, = ax.plot([], [],'o',color = sun.color)
line1, = ax.plot([], [],'o',color = mercury.color)
line2, = ax.plot([], [], 'o',color = venus.color)
line3, = ax.plot([], [], 'o',color = earth.color)
line4, = ax.plot([], [], 'o',color = mars.color)



def init(): # za pokretanje plotanja pridruzuje se prazna lista
    linesun.set_data([],[])
    line1.set_data([],[])
    line2.set_data([],[])
    line3.set_data([],[])
    line4.set_data([],[])
    return line, line1, line2, line3, line4

def animacija(i): # nadodavanje podataka u liste za plotanje putanje
    xs.append(sun.x[i])
    ys.append(sun.y[i])
    xm.append(mercury.x[i])
    ym.append(mercury.y[i])
    xv.append(venus.x[i])
    yv.append(venus.y[i])
    xe.append(earth.x[i])
    ye.append(earth.y[i])
    xm1.append(mars.x[i])
    ym1.append(mars.y[i])

    linesun.set_data(xs[i], ys[i])
    line1.set_data(xm[i], ym[i])
    line2.set_data(xv[i], yv[i])
    line3.set_data(xe[i], ye[i])
    line4.set_data(xm1[i], ym1[i])

    return line, line1, line2, line3, line4

plt.plot(sun.x,sun.y,label=sun.ime_planeta,color=sun.color, linewidth=5.0)
plt.plot(mercury.x,mercury.y,label=mercury.ime_planeta,color=mercury.color)
plt.plot(venus.x,venus.y,label=venus.ime_planeta,color=venus.color)
plt.plot(earth.x,earth.y,label=earth.ime_planeta,color=earth.color)
plt.plot(mars.x,mars.y,label=mars.ime_planeta,color=mars.color)

anim = animation.FuncAnimation(fig, animacija, init_func=init, interval=20, blit = True)
plt.title('Planeti animacija graf')
plt.legend(loc="upper right")
plt.show()

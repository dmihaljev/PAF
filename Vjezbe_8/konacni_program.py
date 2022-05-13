import projectile as pr
import matplotlib.pyplot as plt

p1 = pr.Projectile()
p1.set_init_cond(20,60,0.1,0.3,0.05,0.01)
xe,ye = p1.putanja()

p2 = pr.Projectile()
p2.set_init_cond(20,60,0.1,0.3,0.05,0.01)
x,y = p2.putanja_rk()

plt.plot(xe,ye,label="dt=0.01, Euler")
plt.plot(x,y,label="dt=0.01, Runge-Kutta",c='red')
plt.title('x-y graf')
plt.legend(loc="upper left")
plt.xlabel('x[m]')
plt.ylabel('y[m]')
plt.show()
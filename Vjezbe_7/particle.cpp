#include <iostream>
#include <particle.h>
#include <math.h>

using namespace std;


        void particle::evolve()
        {
            while (y >= 0)
            {
                vx += 0.;
                vy += g * dt;

                x += vx * dt;
                y += vy * dt;

                t += dt;
            }
        }
        particle::particle(double v, double theta, double x0, double y0, double step)
        {
            vx = v*cos(theta*M_PI/180);
            vy = v*sin(theta*M_PI/180);
            x = x0;
            y = y0;
            t = 0.;
            dt = step;
        }
        double particle::range()
        {
            while (t <= dt)
            {
                evolve();
            
            }
            return x;
        }
        double particle::time()
        {
            while(t <= dt)
            {
                evolve();

            }
            return t;
        }


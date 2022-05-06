#include <iostream>
#include <math.h>

using namespace std;

class particle
{
    private:
        double x, y, t, dt, vx, vy, g = -9.81;

        void evolve();
        
    public:
        particle(double v, double theta, double x0, double y0, double step = 0.01);
        
        double range();
        
        double time();
};

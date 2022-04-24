# include <iostream>
# include <math.h>
using namespace std;

bool kruznica (float x, float y, float r, float h, float k) //(h, k) je centar kruznice
{

    float r1 = sqrt((x - h)*(x - h) + (y - k)*(y - k));
    
    bool unutrasnjost;

    if (r1 < r)
    {
        unutrasnjost = true;
    }
    else
    {
        unutrasnjost = false;
    }
    return unutrasnjost;
}

int main()
{   
    if (kruznica(1, 1, 2, 0, 0))cout << "Tocka je unutar kruznice" << endl;
    else cout << "Tocka je unutar kruznice" << endl;
    return 0;
}
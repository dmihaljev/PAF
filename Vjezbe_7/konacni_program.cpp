#include <iostream>
#include <particle.h>

using namespace std;

int main()
{
    particle p1(100, 45, 0, 0);
    particle p2(10, 60, 0, 0);

    cout << "Domet prve cestice je: " << p1.range() << " metra" << endl;
    cout << "Vrijeme trajanja leta prve cestice je: " << p1.time() << " sekundi"<< endl;

    cout << "Domet druge cestice je: " << p2.range() << " metra" <<endl;
    cout << "Vrijeme trajanja leta druge cestice je: " << p2.time() << " sekundi" << endl;

    return 0;
}

#include <iostream>
using namespace std;

bool sustav(int a1, int b1, int c1, int a2, int b2, int c2)
{
    int determintanta, detx, dety;
    int b1predznak, b2predznak;
    bool indeks_det=false;

    b1predznak=b1*(-1);
    b2predznak=b2*(-1);
    if (b1>0)
    {
       cout << a1 <<"x+"<<b1<<"y = "<< c1<< endl;
    }
    else if (b1<0)
    {
       cout<< a1 <<"x-"<<b1predznak<<"y = "<< c1<< endl;
    }
    if (b2>0)
    {
       cout<< a2 <<"x+"<<b2<<"y = "<< c2<< "\n\t\t " <<endl;
    }
    else if (b2<0)
    {
       cout<< a2 <<"x-"<<b2predznak<<"y = "<< c2<< "\n\t\t " << endl;
    }
     
    determintanta=(a1*b2)-(a2*b1);
    detx=(c1*b2)-(c2*b1);
    dety=(a1*c2)-(a2*c1);
    if (determintanta==0 && detx==0 && dety==0) 
    {
        cout<<"Sustav je ovisan"<< endl;
        indeks_det = true;
    }
    else if (determintanta==0 && (detx!=0 || dety!=0))
    {
        cout<<"Sustav je nepotpun"<< endl;
        indeks_det = true;
    }
    
    cout<<"D = "<< determintanta << endl; 
    cout<<"D(x) = "<< detx << endl;
    cout<<"D(y) = "<< dety << endl;

    return 0;
} 
int main()
{
    sustav(1,2,3,2,5,6);
    return 0;
}
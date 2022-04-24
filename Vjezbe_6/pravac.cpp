# include <iostream>
using namespace std;

void pravac(float x1, float y1, float x2, float y2){
    float k = (y2 - y1) / (x2 - x1);
    float l = -k * x1 + y1;

    if(l>0) cout << "Jednadzba pravca je:" "y=" << k << "x+" << l << endl;
    else if(l<0) cout << "Jednadzba pravca je:" "y=" << k << "x" << l << endl;
    else cout << "Jednadzba pravca je:" "y=" << k << endl;
    }
    
int main(){
    
float x1 = 1.0;
float y1 = 2.0;
float x2 = 3.0;
float y2 = 4.0;

pravac(x1, y1, x2, y2);

return 0;
}

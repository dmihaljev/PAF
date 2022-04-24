#include <iostream>
#include <algorithm>
using namespace std;

void interval_polja(float polje[], float N, float a, int b)
{
    for(int i = 0; i < N; i++)
    {
        if(polje[i] >= a && polje[i] <= b)
        {
            cout << polje[i] << endl;
        }
    }
    cout<<endl;
}

void obrtanje_polja(float polje[], int i, int j)
{
    float temp;
    temp = polje[i];
    polje[i] = polje[j];
    polje[j] = temp;
}

int main()
{
    float polje[6] = {1, 4.5, 3.1, 8, 1.6, 2};
    interval_polja(polje, 6, 0., 9.);

    sort(begin(polje), end(polje));
    interval_polja(polje, 6, 0., 9.);
    reverse(begin(polje), end(polje));
    interval_polja(polje, 6, 0., 9.);

    obrtanje_polja(begin(polje), 1, 2);
    interval_polja(polje, 6, 0., 9.);

    return 0;
}


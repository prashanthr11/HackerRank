#include <iostream>
using namespace std;
int main()
{
    int n, rotations;
    cin >> n >> rotations;
    int a[n];
    for(int i = 0; i < n; i++)
    cin >> a[i];
    
    for(int i = 0; i < n; i++) 
        cout << a[(i + rotations) % n] << ' ';
     cout << endl;
}

#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin >> n;
    int a[n], b[n];
    for(int i = 0; i < n; i++)  cin>>a[i];
    for(int i=0;i<n;i++) {
        if(a[i] < 38)
            b[i] = a[i];
        
        else if(a[i] % 5 == 2) {
            b[i] = a[i] + 3;
        }    
        else if(a[i] %5 == 4)
            b[i] = a[i] + 1;
        
        else if(a[i] % 5 == 1)
            b[i] = a[i] + 4;
        
        else if(a[i] % 5 == 3)
            b[i] = a[i] + 2;
        
        else if(a[i] % 5 == 0)
            b[i] = a[i];
    }

    for(int i = 0; i < n; i++) {
        if((b[i] - a[i]) < 3)
            a[i] = b[i];
        else
            b[i] = a[i];
    }
    
    for(int i = 0; i < n; i++)
        cout << a[i] << endl;
    return 0;
}

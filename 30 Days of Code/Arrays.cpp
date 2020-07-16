#include <bits/stdc++.h>

using namespace std;


int main()
{
    int n;
    cin >> n;
    vector<int> a(n);
    for(auto i = 0; i < n; ++i)
        cin >> a[i];

    reverse(a.begin(), a.end());
    
    for(auto i:a)
        cout << i << ' ';

    return 0;
}


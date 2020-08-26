#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;

    unordered_map<int, int> mp;
    
    vector<int> a(n);
    for(auto i = 0; i < n; ++i) {
        cin >> a[i];
        mp[a[i]]++;
    }

    int m;
    cin >> m;

    vector<int> b(m);
    for(auto i = 0; i < m; ++i)
        cin >> b[i];
        
    for(auto i = 0; i < m; ++i) {
        auto tmp = lower_bound(a.begin(), a.end(), b[i]);
        if(mp[b[i]])
            cout << "Yes" << ' ' << 1 + tmp - begin(a) << endl;
        else
            cout << "No" << ' ' << 1 + tmp - begin(a) << endl;
    }
}

# include <bits/stdc++.h>
# define int long long

using namespace std;

void update(int* a, int l, int h, int k) {
    a[l] += k;
    a[h] -= k;
}


signed main() {
    int n, m;
    cin >> n >> m;
    
    auto *a = (int *)malloc(sizeof(int) * (n + 1));
    auto *b = (int *)malloc(sizeof(int) * (n + 1));

    for(auto i = 0; i <= n; ++i)
        a[i] = b[i] = 0;

    for(auto i = 0; i < m; ++i) {
        int x, y, z;
        cin >> x >> y >> z;
        update(a, x - 1, y, z);
    }
    
    auto maxi = b[0] = a[0];
    
    for(auto i = 1; i < n; ++i) {
        b[i] = b[i - 1] + a[i];
        maxi = max(maxi, b[i]);
    }
        
    cout << maxi << endl;
}

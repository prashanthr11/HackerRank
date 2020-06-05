#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, k, q;
    cin >> n >> k >> q;
    vector<int> a(n);
    k = k % n;
    for(int i = 0; i < n; ++i)  cin >> a[i];
    rotate(rbegin(a), rbegin(a) + k, rend(a));
    for(int i =0; i < q; ++i) {
        int x;
        cin >> x;
        cout << a[x] << endl;
    }
}

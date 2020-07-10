#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, q;
    cin >> n >> q;
    vector<vector<int>> ans(n, vector<int> ());

    for(int i = 0; i < n; ++i) {
        int t;
        cin >> t;
        for(int k = 0; k < t; ++k) {
            int as;
            cin >> as;
            ans[i].push_back(as);
        }
    }

    for(int i = 0; i < q; ++i) {
        int x, y;
        cin >> x >> y;
        cout << ans[x][y] << endl;
    }

    return 0;
}

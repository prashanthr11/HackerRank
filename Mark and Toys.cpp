#include <bits/stdc++.h>>

using namespace std;

int main() {
    int n, limit, cnt = 0;
    cin >> n >> limit;
    int a[n];
    for(int i = 0; i < n; i++)
        cin >> a[i];
    
    sort(a, a + n);
    for(int i = 0; i < n; i++) {
        if(limit <= 0) {
            break;
        }
        else if(limit > a[i]) {
            limit-=a[i];
            ++cnt;
        }
    }
    cout << cnt;
}

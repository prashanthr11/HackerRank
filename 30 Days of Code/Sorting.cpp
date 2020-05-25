#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;


int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for(int i = 0; i < n; ++i)
        cin >> a[i];

    int cnt = 0;
    for(int i = 1; i < a.size(); ++i) {
        if(a[i] < a[i - 1]) {
            cnt++;
            swap(a[i], a[i - 1]);
            i = 0;
        }
    }
    cout << "Array is sorted in " << cnt << " swaps." << endl;
    cout << "First Element: " << a[0] << endl;
    cout << "Last Element: " << a[n - 1] << endl;
    return 0;
}
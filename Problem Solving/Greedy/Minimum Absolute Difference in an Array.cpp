#include<bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for(int i=0; i < n; i++)
        cin >> a[i];
    sort(begin(a), end(a));
    int mini = INT_MAX;
    for(int i = 0; i < n; i++)
        mini = min(mini, abs(a[i] - a[i + 1]));
        
    cout << mini << endl; 
}
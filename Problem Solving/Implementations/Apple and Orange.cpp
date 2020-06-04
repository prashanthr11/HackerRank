#include <bits/stdc++.h>
using namespace std;
int main() {
    int a, b, s, t, m, n, cnt = 0;
    cin >> s >> t >> a >> b >> m >> n;
    int arr[m], brr[n];
    for(int i = 0; i < m; i++){
        cin >> arr[i];
        arr[i] += a;
    }
    for(int i = 0; i < n; i++){
        cin >> brr[i];
        brr[i] += b;
    }
    for(int i = 0; i < m; i++){
        if(arr[i] >= s && arr[i] <= t){
            cnt++;
        }
    }
    cout << cnt << endl;
    int flag = 0;
    for(int i = 0; i < n; i++){
        if(brr[i] <= t && brr[i] >= s){
            flag++;
        }
    }
    cout<< flag <<endl;
}

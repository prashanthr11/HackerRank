#include <algorithm>
#include <iostream>
#include <vector>
#include<unordered_map>

using namespace std;

int main() {
    int n;
    cin >> n;
    unordered_map<int, int> mp;
    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        mp[x]++;
    }

    bool flag = false;
    for(auto i:mp) {
        if(i.second > n/2) {
            flag = true;
            break;
        }
        else
        flag = false;
    }

    if(flag)
    cout << int(flag) << endl;
    else
    cout << int(flag) << endl;
}

#include <iostream>
#include <string.h>
# include <unordered_map>

using namespace std;
int main() {
    int t;
    cin >> t;
    while(t--) {
        string s, s2;
        unordered_map<char, int> mp;
        cin >> s >> s2;
        
        for(int i = 0; i < s.length(); ++i)
        mp[s[i]]++;

        bool flag = false;

        for(int i = 0; i < s2.length(); ++i) {
            if(mp[s2[i]]) {
                flag = true;
                break;
            }
        }
        if(flag)
        cout << "YES" << endl;
        else
        cout << "NO" << endl;
    }
}

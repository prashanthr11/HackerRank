#include <bits/stdc++.h>

using namespace std;

int main(){
    string str;
    vector<char> str2;
    cin >> str;
    stack<char> s;
    for(auto i:str) {
        if(s.empty())
            s.push(i);
        else if(s.top() == i) 
            s.pop();
        else
        s.push(i);
    }
    
    if(s.size()) {
        while(!s.empty()) {
            str2.push_back(s.top());
            s.pop();
        }
        reverse(str2.begin(), str2.end());
        for(auto x:str2)
            cout << x;
    }
    else
    cout << "Empty String" << endl;
}

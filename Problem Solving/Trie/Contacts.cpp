#include <bits/stdc++.h>

using namespace std;

struct trie {
    struct trie *a[26];
    int count[26] = {0};
};

void add(struct trie *root, string s) {
    auto tmp = root;
    for(auto i:s) {
        if(tmp -> a[i - 'a']) {
            tmp -> count[i - 'a']++;
            tmp = tmp -> a[i - 'a'];
        }
        else {
            auto temp = new struct trie();
            tmp -> a[i - 'a'] = temp;
            tmp -> count[i - 'a']++;
            tmp = temp;
        }
    }
}


int present(struct trie *root, string s) {
    auto tmp = root;
    int cnt = 0;
    
    for(auto i:s) {
        if(!tmp -> a[i - 'a'])
            return tmp -> count[i - 'a'];
        else{
            cnt = tmp -> count[i - 'a'];
            tmp = tmp -> a[i - 'a'];
        }
    }
    
    tmp = root;
    
    return cnt;
}
int main() {
    int n;
    cin >> n;
    auto root = new struct trie();

    for(auto i = 0; i < n; ++i) {
        string s, s1;
        cin >> s >> s1;
        if(s == "add") 
            add(root, s1);
        
        else 
            cout << present(root, s1) << '\n';
    }
}

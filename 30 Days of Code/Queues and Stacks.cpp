#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
        stack<int> stk;
        queue<int> q;
        void pushCharacter(char s) {
            stk.push(s);
        }

        char popCharacter() {
                char t = stk.top();
                stk.pop();
                return t;
        }

        void enqueueCharacter(char s) {
            q.push(s);
        }

        char dequeueCharacter() {
            char t = q.front();
            q.pop();
            return t;
        }
};

int main() {
    // read the string s.
    string s;
    getline(cin, s);
    
  	// create the Solution class object p.
    Solution obj;
    
    // push/enqueue all the characters of string s to stack.
    for (int i = 0; i < s.length(); i++) {
        obj.pushCharacter(s[i]);
        obj.enqueueCharacter(s[i]);
    }
    
    bool isPalindrome = true;
    
    // pop the top character from stack.
    // dequeue the first character from queue.
    // compare both the characters.
    for (int i = 0; i < s.length() / 2; i++) {
        if (obj.popCharacter() != obj.dequeueCharacter()) {
            isPalindrome = false;
            
            break;
        }
    }
    
    // finally print whether string s is palindrome or not.
    if (isPalindrome) {
        cout << "The word, " << s << ", is a palindrome.";
    } else {
        cout << "The word, " << s << ", is not a palindrome.";
    }
    
    return 0;
}

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Difference {
    private:
    vector<int> elements;
  
  	public:
  	int maximumDifference;

	// Add your code here
    Difference(vector<int>& a) {
        elements = a;
    }
    
    void computeDifference() {
        for(auto i = elements.begin(); i != elements.end(); ++i) {
            for(auto j = elements.begin() + 1; j != elements.end(); ++j)
                maximumDifference = max(maximumDifference, abs(*j - *i));
        }
    }
    

}; // End of Difference class

int main() {
    int N;
    cin >> N;
    
    vector<int> a;
    
    for (int i = 0; i < N; i++) {
        int e;
        cin >> e;
        
        a.push_back(e);
    }
    
    Difference d(a);
    
    d.computeDifference();
    
    cout << d.maximumDifference;
    
    return 0;
}

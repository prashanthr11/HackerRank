#include <bits/stdc++.h>

using namespace std;


void print(const vector<int>& n) {
    for(auto i:n) 
        cout << i << ' ';
}

int main()
{
    vector<int> a = {43, 45, 41, 12, 5, 11, 76, 82, 34, 25, 86, 90, 120, 131, 68};
    
    cout << "Vector Elements are :";
    
    print(a);
    
    make_heap(a.begin(), a.end());  // Max heap
    
    // make_heap(a.begin(), a.end(), greater<>());  // Min heap
    
    cout << endl << endl << "Max Heap :";
    
    print(a);
    
    cout << endl << endl << "Root element is :" << a.front();
    
    cout << endl << endl << "Root is deleted (Modified Max Heap) :";

    pop_heap(begin(a), end(a)); // Max Heap: Root is swapped with the last position of the vector
    
    // pop_heap(begin(a), end(a), greater<>());    //Min Heap
    
    print(a);
    
    a.pop_back();   // Deleting the last element in the vector 
    
    cout <<  endl << endl << "Modified Vector Elements are :";
    
    print(a);
    
    a.push_back(134);
    
    //Max Heap
    push_heap(a.begin(), a.end());  // works only with the one element.
                                    //If you try to push more than 1 element the push_heap() will only checks the last element with the parent node.
                                    // or use make_heap()
    
    
    //Min Heap
    // push_heap(a.begin(), a.end(), greater<>()); 
    cout << endl << endl << "After new elements inserted into vector. " <<  endl << "Max Heap :";
    
    print(a);

    
    return 0;
}

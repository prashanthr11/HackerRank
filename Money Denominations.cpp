#include <iostream>
using namespace std;

int b, count = 0,c = 0, d;

int check(int a)
{
    if(a >= 5) {
        b = a % 5;    // No of 5's
        check(b);
    }
    else if(a < 5)
    {
        
        b = a;    // No of 1's
        
    }
    c++;
    return c,b;
}
int get_change(int money) {
    d = money / 10;     // No of 10's
    int a = money % 10;
    check(a);
    count = d + b + c - 1;
  return count;
}


int main() {
  int money;
  cout << "Enter Money: ";
  cin >> money;
  cout << " The Denominations of no of 10's , 5's and 1's are :" << get_change(money) << endl;
}

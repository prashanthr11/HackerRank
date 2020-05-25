#include <bits/stdc++.h>

using namespace std;

// Complete the solve function below.
void solve(float meal_cost, int tip_percent, int tax_percent) {

int sum = meal_cost + meal_cost * (tax_percent) / 100 + meal_cost * (tip_percent) /100;

if(sum==12)
{
    cout<<round(sum)+1;
}
else
cout<<round(sum);
}

int main()
{
    float meal_cost;
    cin >> meal_cost;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int tip_percent;
    cin >> tip_percent;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int tax_percent;
    cin >> tax_percent;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    solve(meal_cost, tip_percent, tax_percent);

    return 0;
}
#include <iostream>
#include <climits>
using namespace std;

int main()
{
    int n = 6, m = 6;
    int a[n][m];
    for(int i = 0;i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> a[i][j];
        }
    }

    int b[n - 2][m - 2];

    for(int i = 1;i < n - 1; i++){
        for (int j = 1;j < m - 1; j++){
            int sum = 0;
            for(int k = -1; k < 2; ++k){
                if(k == 0)continue;
                for(int m = -1; m < 2; ++m){
                    sum += a[i + k][j + m];
                }
            }
            b[i - 1][j - 1] = sum + a[i][j];
        }
    }
    int maxi = INT_MIN;
    for(int i = 0;i < n -2; i++){
        for(int j = 0; j < m - 2; j++){
            maxi = max(maxi, b[i][j]);
        }
    }
    std::cout <<  maxi << std::endl;
}


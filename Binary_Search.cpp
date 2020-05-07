#include <iostream>
#include <cassert>
#include <vector>

using namespace std;


int Binary_Search (int arr[] ,int key ,int minimum, int maximum) {
  if (maximum >= minimum) {

    int middle = minimum + (maximum - minimum) / 2;
    if (key == arr[middle])
    return middle;

    if (key < arr[middle])
    return Binary_Search(arr, key, minimum ,middle-1);

    if (key > arr[middle])
    return Binary_Search(arr, key, middle+1, maximum);
  }
  else
  return -1;
}




int main() {
  int n;
  std::cin >> n;
  int a[n];
  for (int i = 0; i < n; i++)
    std::cin >> a[i];

  int m;
  std::cin >> m;

  int b[m];
  for (int i = 0; i < m; ++i)
    std::cin >> b[i];

  for (int i = 0; i < m; ++i) {
    std::cout << Binary_Search(a, b[i], 0, n) << ' ';
  }
}

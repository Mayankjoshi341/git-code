#include <iostream>

using namespace std;

int binarySearch(int array[], int x, int low, int high) {
  if (low > high) {
    return -1;
  }

  int mid = low + (high - low) / 2;

  if (array[mid] == x) {
    return mid; // Element found at middle
  } else if (array[mid] > x) {
    return binarySearch(array, x, low, mid - 1); 
  } else {
    return binarySearch(array, x, mid + 1, high); 
}

int main() {
  int array[] = {2, 3, 4, 5, 6, 7, 8};
  int x = 3;
  int n = sizeof(array) / sizeof(array[0]);

  int result = binarySearch(array, x, 0, n - 1);

  if (result == -1) {
    cout << "Element is not found" << endl;
  } else {
    cout << "Element is found at index " << result << endl;
  }

  return 0;
}

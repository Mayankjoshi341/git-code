#include <iostream>

using namespace std;

class fractional_knapsack {
public:
  void getdata() {
    cout << "Enter the maximum weight of the bag: ";
    cin >> w;
    cout << "How many objects you want to store inside the bag: ";
    cin >> n;

    cout << "Enter the weights of the objects:\n";
    for (int i = 1; i <= n; i++) {
      cin >> wt[i];
    }

    cout << "Enter the profits of the objects:\n";
    for (int i = 1; i <= n; i++) {
      cin >> pt[i];
    }
  }

  void sortdata() {
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        if ((pt[j] / wt[j]) < (pt[j + 1] / wt[j + 1])) {
          swap(pt[j], pt[j + 1]);
          swap(wt[j], wt[j + 1]);
        }
      }
    }
  }

  void calculation() {
    for (int i = 0; i < n; i++) {
      y[i] = 0.0;
    }
    u = w;

    for (int i = 0; i < n; i++) {
      if (wt[i] > u) {
        break;
      }
      y[i] = 1.0;
      u -= wt[i];
    }

    if (i < n) {
      y[i] = u / wt[i];
    }

    profit = 0.0;
    for (int i = 0; i < n; i++) {
      profit += (pt[i] * y[i]);
    }
  }

  void displaydata() {
    cout << "-------------------------------------------\n";
    cout << "Object No.  Weight   Profit\n";
    cout << "-------------------------------------------\n";
    for (int i = 1; i <= n; i++) {
      cout << i << "\t" << wt[i] << "\t" << pt[i] << "\t" << endl;
    }
    cout << "MAXIMUM PROFIT: " << profit << endl;
  }

private:
  float wt[20], pt[20], profit = 0.0, y[20];
  int n, w, u, temp;
};

int main() {
  fractional_knapsack obj;
  obj.getdata();
  obj.sortdata();
  obj.calculation();
  obj.displaydata();
  return 0;
}

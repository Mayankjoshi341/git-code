#include <iostream>

using namespace std;

int main() {
  int z[2][2];
  int i, j;
  int m1, m2, m3, m4, m5, m6, m7;

  int x[2][2] = {
    {12, 34},
    {22, 10}
  };
  int y[2][2] = {
    {3, 4},
    {2, 1}
  };

  cout << "The first matrix is: " << endl;
  for (i = 0; i < 2; i++) {
    for (j = 0; j < 2; j++) {
      cout << x[i][j] << " ";
    }
    cout << endl;
  }

  cout << "\nThe second matrix is: " << endl;
  for (i = 0; i < 2; i++) {
    for (j = 0; j = 0; j++) {
      cout << y[i][j] << " ";
    }
    cout << endl;
  }

  m1 = (x[0][0] + x[1][1]) * (y[0][0] + y[1][1]);
  m2 = (x[1][0] + x[1][1]) * y[0][0];
  m3 = x[0][0] * (y[0][1] - y[1][1]);
  m4 = x[1][1] * (y[1][0] - y[0][0]);
  m5 = (x[0][0] + x[0][1]) * y[1][1];
  m6 = (x[1][0] - x[0][0]) * (y[0][0] + y[0][1]);
  m7 = (x[0][1] - x[1][1]) * (y[1][0] + y[1][1]);

  z[0][0] = m1 + m4 - m5 + m7;
  z[0][1] = m3 + m5;
  z[1][0] = m2 + m4;
  z[1][1] = m1 - m2 + m3 + m6;

  cout << "\nProduct achieved using Strassen's algorithm: " << endl;
  for (i = 0; i < 2; i++) {
    for (j = 0; j < 2; j++) {
      cout << z[i][j] << " ";
    }
    cout << endl;
  }

  return 0;
}

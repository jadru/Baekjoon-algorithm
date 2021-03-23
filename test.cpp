#include <iostream>
using namespace std;

int main() {
    int a1, a2, a3, cal;
    cin >> a1; cin >> a2; cin >> a3;
    cal = a1 * a2 * a3;
    int out[11] = { 0, };
    for (int i = 100000000; i >= 10; i/=10){
        int j = cal / i;
        out[j]++;
    }
    for (int i = 0; i < 10; i++){
        cout << out[i] << endl;
    }
    cout << cal;
    return 0;
}
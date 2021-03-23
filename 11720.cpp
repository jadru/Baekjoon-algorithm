#include <iostream>
using namespace std;

int main() {
    int a, cnt = 0;
    cin >> a;
    char c[a+1];
    cin >> c;
    for(int i = 0; i < a; i++){
        cnt += c[i] - '0';
        if (c[i]=='\0')
            break;
    }
    cout << cnt;
    return 0;
}
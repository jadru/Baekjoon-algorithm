#include <iostream>
using namespace std;

int main() {
    int a[5];
    for(int i = 0; i < 5; i++){
        cin >> a[i];
    }
    int cal = 1;
    while(true){
        int cnt = 0;
        for(int i = 0; i < 5; i++){
            if(cal % a[i] == 0)
                cnt++;
            if(cnt >= 3){
                cout << cal;
                return 0;
            }
        }
        cal++;
    }
}

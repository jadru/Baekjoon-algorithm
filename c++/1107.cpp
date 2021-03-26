#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int N = 100, broken_btn_cnt, cn_d_int, cnt = 0;
    int NUMS[10] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    cin >> cn_d_int;
    char* cn_destination;
    cin >> broken_btn_cnt;
    int broken_btn[broken_btn_cnt];
    for(int i = 0; i < broken_btn_cnt; i++){
        cin >> broken_btn[i];
    }
    for(int i = 0; i < broken_btn_cnt; i++){
        for(int j = 0; j < 10; j++){
            if(broken_btn[i] == NUMS[j])
                NUMS[j] = -1;
        }
    }
    for(int i = 0; i < broken_btn_cnt; i++){
        int min_cnt = 10, min;
        for(int j = 0; j < 10; j++){
            if(NUMS[j] == -1)
                continue;
            else{
                if(min > abs((int)cn_destination[i] - j)){
                    min_cnt = (int)cn_destination[i] - j;
                    min = (int)cn_destination[i];
                    cout << min << endl;
                }
            }
        }
    }
    
    cout << cnt;
    return 0;
    
}

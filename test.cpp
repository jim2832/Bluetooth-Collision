#include <iostream>
#include <string>
#include <math.h>
#include <cstdlib> /* 亂數相關函數 */
#include <ctime>   /* 時間相關函數 */
using namespace std;

int main(){
    int arr[2];
    srand(time(NULL));
    for(int i=0; i<20; i++){

        /* 指定亂數範圍 */
        int channel_num = 79;

        int rand_num = rand() % (channel_num + 1);
        
    }

    return 0;
}
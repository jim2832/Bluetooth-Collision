#include <iostream>
#include <string>
#include <math.h>
#include <cstdlib> /* 亂數相關函數 */
#include <ctime>   /* 時間相關函數 */
using namespace std;

int main(){
    for(int i=0; i<10; i++){
        //srand(time(NULL));

        /* 指定亂數範圍 */
        int min = 0;
        int max = 79;

        /* 產生 [min , max] 的整數亂數 */
        int x = rand() % (max - min + 1) + min;

        cout << x << endl;
    }

    return 0;
}
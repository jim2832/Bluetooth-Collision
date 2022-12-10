#include <iostream>
#include <string>
#include <math.h>
using namespace std;

#define MAX_DEV_NUM 100

int main(){
    //int *device = new int[MAX_DEV_NUM]; //裝置
    int device_num[] = {2}; //裝置的數量
    cout << sizeof(device_num)/sizeof(device_num[0]) << endl; //print 1 (目前模擬了幾種裝置)

    for(int i=0; i<sizeof(device_num)/sizeof(device_num[0]); i++){
        int *device = new int[device_num[i]]; //儲存裝置的陣列
        cout << sizeof(device) / sizeof(device[0]) << endl; //print 2 (當前模擬裝置的數量)

        //模擬200次
        for(int sim_cnt=0; sim_cnt<200; sim_cnt++){
            //每次跳頻1600次
            for(int freq=0; freq<1600; freq++){

            }
        }
        
        
        delete[] device;
    }
    

    return 0;
}
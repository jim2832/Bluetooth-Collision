#include <iostream>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
using namespace std;

#define MAX_DEV_NUM 100
#define CHANNEL 79

void clean_array(int *arr){
    int len = sizeof(arr)/sizeof(int);
    for(int i=0; i<len; i++){
        arr[i] = 0;
    }
}


int main(){
    //int *device = new int[MAX_DEV_NUM]; //裝置
    int device_num[] = {2}; //裝置的數量
    int *channel_seq = new int[MAX_DEV_NUM]; //儲存碰撞的陣列
    int collision_cnt = 0; //碰撞次數
    srand(time(NULL)); //隨機seed

    for(int i=0; i<sizeof(device_num)/sizeof(device_num[0]); i++){
        int *device = new int[device_num[i]]; //儲存裝置的陣列
        //cout << sizeof(device)/sizeof(device[0]) << endl; //print 2 (當前模擬裝置的數量)

        //模擬200次
        for(int sim_cnt=0; sim_cnt<200; sim_cnt++){
            //每個模擬跳頻1600次
            for(int freq=0; freq<1600; freq++){
                //各個裝置
                for(int dev=0; dev<sizeof(device)/sizeof(device[0]); dev++){
                    int rand_num = rand() % (CHANNEL + 1);
                    //cout << rand_num << endl;
                    channel_seq[dev] = rand_num;
                    if(dev > 0){
                        cout << channel_seq[dev-1] << "\t" << channel_seq[dev];
                        if(channel_seq[dev-1] == channel_seq[dev]){
                            collision_cnt++;
                            cout << "\t<- Collision!" << endl;
                        }
                        else{
                            cout << endl;
                        }
                        clean_array(channel_seq);
                    }
                }
            }
        }
        cout << endl << "有2個裝置的碰撞次數為: " << collision_cnt << endl;
        sleep(1);
        
        
        delete[] device;
    }

    delete[] channel_seq;

    return 0;
}
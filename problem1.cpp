#include <iostream>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
using namespace std;

#define SIM_CNT 200
#define HOPPING_FREQENCY 1600
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
    int *channel_seq = new int[MAX_DEV_NUM]; //儲存測試的陣列
    int *collision_seq = new int[MAX_DEV_NUM]; //儲存碰撞的陣列
    int *total_time = new int[MAX_DEV_NUM]; //總次數
    double *Prob = new double[MAX_DEV_NUM]; //碰撞機率
    int collision_cnt = 0; //碰撞次數
    srand(time(NULL)); //隨機seed

    for(int i=0; i<sizeof(device_num)/sizeof(device_num[0]); i++){ //目前sizeof(device_num)/sizeof(device_num[0]) = 1
        int *device = new int[device_num[i]]; //儲存裝置的陣列
        //cout << sizeof(device)/sizeof(device[0]) << endl; //print 2 (當前模擬裝置的數量)

        //模擬200次
        for(int sim_cnt=0; sim_cnt<SIM_CNT; sim_cnt++){
            //每個模擬跳頻1600次
            for(int freq=0; freq<HOPPING_FREQENCY; freq++){
                //各個裝置
                for(int dev=0; dev<sizeof(device)/sizeof(device[0]); dev++){
                    int rand_num = rand() % (CHANNEL + 1);
                    //cout << rand_num << endl;
                    channel_seq[dev] = rand_num;
                    if(dev > 0){
                        cout << channel_seq[dev-1] << "\t" << channel_seq[dev];
                        if(channel_seq[dev-1] == channel_seq[dev]){
                            collision_cnt++;
                            //cout << "\t<- Collision!" << endl;
                        }
                        // else{
                        //     cout << endl;
                        // }
                        clean_array(channel_seq);
                    }
                }
            }
        }
        //cout << endl << "有2個裝置的碰撞次數為: " << collision_cnt << endl;

        collision_seq[i] = collision_cnt;
        total_time[i] = SIM_CNT * HOPPING_FREQENCY * device_num[i];
        Prob[i] = (double)collision_seq[i] / total_time[i];
        cout << total_time[i] << endl;
        cout << "有 " << device_num[i] << " 個裝置的碰撞機率為: "  << Prob[i] << endl;
        
        delete[] device;
    }

    delete[] channel_seq;
    delete[] collision_seq;
    delete[] Prob;

    return 0;
}
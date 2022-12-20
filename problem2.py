import random
import math
import time
import matplotlib.pyplot as plt

SIM_CNT = 30
HOP_FREQ = 1600
DEVICE_CNT = 60

threshold = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
bad_channel_cnt = [] #代表threshhold為0.1到0.9的bad channel數量
channel = [i for i in range(80)] #1~79的channel

device_select_channel = [] #device_select_channel[0]代表是device 0挑到的channel
total_channel_collision = [0] * 100 #每個channel碰撞的次數
channel_collision_prob = [0] * 80 #每個channel碰撞的機率

is_bad_channel = [False] * 80 #壞掉的channel
is_bad_channel[random.randint(1,79)] = True #隨機選受到干擾的頻道
#print(bad_channel[0])

#假設現在是20個裝置
#模擬30秒
for sim in range(SIM_CNT):
    #每一秒跳頻1600次
    collision_every_sec = [0] * 100 #每一秒每個channel的碰撞次數
    for freq in range(HOP_FREQ):
        #20個裝置，建立一個list存每個裝置選到的channel
        for dev in range(DEVICE_CNT):
            device_select_channel.append(random.randint(1, 80))
        #print(device_select_channel)

        #判斷是否有碰撞，如果有，則紀錄某個channel的碰撞次數
        for i in range(len(device_select_channel)):
            for j in range(len(device_select_channel)):
                if i != j and device_select_channel[i] == device_select_channel[j]:
                    total_channel_collision[device_select_channel[i]] = total_channel_collision[device_select_channel[i]] + 1
                    #collision_every_sec[device_select_channel[i]] = collision_every_sec[device_select_channel[i]] + 1
        device_select_channel.clear()
    
    #判斷是否為bad channel
    # for i in range(1,80):
    #     #印出每一秒每個channel的碰撞次數
    #     print(collision_every_sec[i], " ", end="")
    # print("\n")
    # time.sleep(1)
    #collision_every_sec.clear()

#印出每個channel的碰撞次數和機率
for i in range(1,80):
    #print(f"channel{i}:",total_channel_collision[i],"次collision")
    channel_collision_prob[i] = total_channel_collision[i]/(SIM_CNT*HOP_FREQ)
    print(f"channel {i} 的碰撞機率為:",round(channel_collision_prob[i], 5))

#畫出每個channel的碰撞機率
plt.bar(channel[1:79], channel_collision_prob[1:79])
plt.title("The collision probability of every channel") # title
plt.xlabel("channel") # x label
plt.ylabel("collision probability") # y label
plt.show()
import random
import time
import matplotlib.pyplot as plt

SIM_CNT = 30
HOP_FREQ = 1600

collision = 0

device_num = [20, 30, 40, 50, 60, 70]
threshold = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
device_select_channel = [] #device_select_channel[0]代表是device 0挑到的channel
channel_collision = [0] * 100

bad_channel = []
bad_channel.append(random.randint(1, 80)) #選受到干擾的頻道
#print(bad_channel[0])

#假設現在是20個裝置
#模擬30秒
for sim in range(SIM_CNT):
    #每一秒跳頻1600次
    for freq in range(HOP_FREQ):
        #20個裝置，建立一個list存每個裝置選到的channel
        for dev in range(70):
            device_select_channel.append(random.randint(1, 80))
        #print(device_select_channel)

        #判斷是否有碰撞，如果有，則紀錄某個channel的碰撞次數
        for i in range(len(device_select_channel)):
            for j in range(len(device_select_channel)):
                if i != j and device_select_channel[i] == device_select_channel[j]:
                    channel_collision[device_select_channel[i]] = channel_collision[device_select_channel[i]] + 1

        device_select_channel.clear()

#印出每個channel的碰撞次數
for i in range(1,80):
    print(channel_collision[i], end="")
    print(" ", end="")
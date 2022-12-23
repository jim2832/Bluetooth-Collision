import random
import math
import time
import matplotlib.pyplot as plt

SIM_CNT = 30
HOP_FREQ = 1600
DEVICE_CNT = 70

device_select_channel = [] #device_select_channel[0]代表是device 0挑到的channel
total_channel_collision = [0 for i in range(80)] #每個channel碰撞的次數
channel_collision_prob = [0 for i in range(80)] #每個channel碰撞的機率

"""
前4秒的 bad channel 機率
"""
for sim in range(4):
    #每一秒跳頻1600次
    for freq in range(HOP_FREQ):

        #n個裝置
        for dev in range(DEVICE_CNT):
            device_select_channel.append(round((random.randint(1,79)+random.randint(1,79))/2))
        
        #判斷是否有碰撞，如果有，則紀錄某個channel的碰撞次數
        for i in range(len(device_select_channel)):
            for j in range(len(device_select_channel)):
                if i != j and device_select_channel[i] == device_select_channel[j]:
                    total_channel_collision[device_select_channel[i]] += 1
                    #collision_every_sec[device_select_channel[i]] = collision_every_sec[device_select_channel[i]] + 1
        
        device_select_channel.clear()

for i in range(1,80):
    channel_collision_prob[i] = round(total_channel_collision[i]/(4*HOP_FREQ),2)
#print(total_channel_collision)

"""
後26秒的碰撞機率
"""

import random
import math
import collections
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
for sec in range(4):
    #每一秒跳頻1600次
    for freq in range(HOP_FREQ):

        #n個裝置，建立一個list存每個裝置選到的channel
        for dev in range(DEVICE_CNT):
            #device_select_channel.append(random.randint(1, 79))
            device_select_channel.append(round((random.randint(1,79)+random.randint(1,79)+random.randint(1,79))/3))
        
        #判斷是否有碰撞，如果有，則紀錄某個channel的碰撞次數
        for i in range(len(device_select_channel)):
            for j in range(len(device_select_channel)):
                if i != j and device_select_channel[i] == device_select_channel[j]:
                    total_channel_collision[device_select_channel[i]-1] += 1
                    #collision_every_sec[device_select_channel[i]] = collision_every_sec[device_select_channel[i]] + 1
        
        device_select_channel.clear()

for i in range(79):
    channel_collision_prob[i] = round(total_channel_collision[i]/(4*HOP_FREQ), 2)
#print(total_channel_collision)


"""
後26秒的碰撞機率
"""
collision = [[] for i in range(9)] #紀錄佔用的個數
for i in range(len(collision)):
    for j in range(79):
        collision[i].append(0)
device_channel = [[] for i in range(9)] #紀錄device選的channel
device_collision = [{} for i in range(9)]
threshold = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

good_channel = []
closest = 78

#26秒
for sec in range(26):
    #每秒跳頻1600次
    for freq in range(HOP_FREQ):
        
        #n個裝置
        for dev in range(DEVICE_CNT):
            selected_channel = random.randint(1, 79)
            # i=1~9跑 threshold、device_channel
            for i in range(9):
                good_channel.clear()
                closest = 78
                #如果選到的 channel 為 bad channel
                if(channel_collision_prob[selected_channel] > threshold[i]):
                    #尋找非 bad channel 來做 mapping
                    for j in range(len(channel_collision_prob)):
                        if(channel_collision_prob[j] < threshold[i]):
                            good_channel.append(j+1)
                            #計算最近的channel
                            if(abs(selected_channel - (j+1)) < closest):
                                closest = abs(selected_channel - (j+1))
                    
                    #如果沒有normal channel，則隨機挑選一個
                    if(len(good_channel) != 0):
                        #判斷要往前還是往後mapping
                        if(selected_channel + closest <= 79):
                            target = selected_channel + closest
                        else:
                            target = selected_channel - closest
                        #判斷要 remapping 到哪個 channel
                        forward = selected_channel + closest
                        backward = selected_channel - closest
                        if(channel_collision_prob[target] < threshold[i]):
                            if(forward <= 79):
                                device_channel[i].append(forward)
                            else:
                                device_channel[i].append(backward)
                        else:
                            device_channel[i].append(backward)
                    else:
                        device_channel[i].append(selected_channel)
                else:
                    device_channel[i].append(selected_channel)

        #判斷碰撞
        for k in range(9):
            device_collision[k] = collections.Counter(device_channel[k])
            for channel,times in device_collision[k].items():
                if(times > 1):
                    collision[k][channel-1] += times-1
            device_collision[k].clear()
            device_channel[k].clear()


"""
output
"""
output_collision = []
for i in range(9):
    output_collision.append(sum(collision[i])/(26*HOP_FREQ)/79)
plt.bar(threshold, output_collision, width=0.015)
plt.xlabel("threshold")
plt.ylabel("collision probability")
plt.title(f"device number = {DEVICE_CNT}")
plt.show()
import random
import math
import time
import matplotlib.pyplot as plt

SIM_CNT = 30
HOP_FREQ = 1600
DEVICE_CNT = 50

threshold = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
bad_channel_cnt = [0 for i in range(9)] #bad channel的數量

device_select_channel = [] #device_select_channel[0]代表是device 0挑到的channel
total_channel_collision = [0 for i in range(80)] #每個channel碰撞的次數
channel_collision_prob = [0 for i in range(80)] #每個channel碰撞的機率

"""
process
"""
#選出40個容易受到干擾的channel
interfered_channel = []
while(len(interfered_channel) < 40):
    rand = random.randint(1,79)
    if rand not in interfered_channel:
        interfered_channel.append(rand)
#從40個中選出1個bad channel
selected_bad_channel = random.choice(interfered_channel)

#模擬30秒
for sim in range(SIM_CNT):
    #每一秒跳頻1600次
    for freq in range(HOP_FREQ):

        #20個裝置，建立一個list存每個裝置選到的channel
        for dev in range(DEVICE_CNT):
            device_select_channel.append(random.randint(1, 79))
            #device_select_channel.append(round((random.randint(1,79)+random.randint(1,79)+random.randint(1,79))/3))
        #print(device_select_channel)

        #判斷是否有碰撞，如果有，則紀錄某個channel的碰撞次數
        for i in range(len(device_select_channel)):
            for j in range(len(device_select_channel)):
                if i != j and device_select_channel[i] == device_select_channel[j]:
                    total_channel_collision[device_select_channel[i]-1] += 1
                    #collision_every_sec[device_select_channel[i]] = collision_every_sec[device_select_channel[i]] + 1
        
        device_select_channel.clear()

#印出每個channel的碰撞次數和機率
for i in range(79):
    #print(f"channel{i}:",total_channel_collision[i],"次collision")
    channel_collision_prob[i] = total_channel_collision[i]/(SIM_CNT*HOP_FREQ)
    print(f"channel {i+1} 的碰撞機率為:", round(channel_collision_prob[i], 5))


#判斷bad channel
for i in range(79):

    #被選中的bad channel
    if(i == selected_bad_channel):
        temp = math.floor(channel_collision_prob[i] * 10)
        for k in range(temp, 8):
            bad_channel_cnt[k] += 1
    
    #其他的channel
    for j in range(len(threshold)):
        if(channel_collision_prob[i] > threshold[j]):
            bad_channel_cnt[j] += 1


"""
output
"""
channel = [i for i in range(79)] #1~79的channel

plt.figure(figsize=(10,4))
plt.figure(1)
collision_graph = plt.subplot(121)
bad_channel_graph = plt.subplot(122)

#畫出每個channel的碰撞機率
collision_graph.bar(channel[1:79], channel_collision_prob[1:79], width=0.5)
collision_graph.xaxis.set_label_text("channel") #x label
collision_graph.yaxis.set_label_text("collision probability") #y label

#畫出每個threshold會有的bad channel數量
bad_channel_graph.bar(threshold, bad_channel_cnt, width=0.03)
bad_channel_graph.xaxis.set_label_text("threshold") #x label
bad_channel_graph.yaxis.set_label_text("bad channel count") #y label

plt.suptitle(f"{DEVICE_CNT} devices")
plt.show()
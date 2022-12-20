import random
import collections
import math
import matplotlib.pyplot as plt

# -----<step1 cal data>-----
# noise bad channel(P = 0.3) 
# 一定時間內，x個channel被干擾的情況為P=0.3
# λ=0.49~0.52/1.16~1.2 x=1 平均發生次數為λ
# 1個channel被干擾的情況約為0.3

# 選出40容易受干擾的channel
interference_channel=[]
while(len(interference_channel)<40):
    x=random.randint(1,79)
    if x not in interference_channel:
        interference_channel.append(x)
# 從40選出1
bad_index=random.choice(interference_channel)

# host bad channel
# 這個 channel 在 30secs(30*1600) 被佔用了幾次

# initial list
result_collision=[]
result_occpuy=[]
for i in range(79):
    result_collision.append(0)  # 存放id被碰撞的次數
    result_occpuy.append(0)     # 存放id被占用的次數

host_num=0      # 機器數量
host_index=[]   # 存放機器占用channel id
collision={}    # 統計使用到的channel id 各有幾個

for i in range(48000):
    host_num=0
    # TODO random N host channel for single time 
    while(host_num<70): 
        host_channel=round((random.randint(1,79)+random.randint(1,79))/2)
        host_index.append(host_channel) # save channel
        host_num+=1
    collision=collections.Counter(host_index) # change to dictionary(channel id,times<有幾個host使用此id>)
    
    # save and read data
    for key,value in collision.items():
        result_occpuy[key-1]+=1 # save total host used times 
        
        if(value>1): # save collision times
            result_collision[key-1]+=value-1
   
    host_index.clear()
    collision.clear()

# -----<step2 output>-----
#建立畫布
plt.figure(figsize=(8,7))

#第一張圖
# y range - channel avg collision count
for i in range(79):
    result_collision[i]=round(result_collision[i]/48000,4)
# x range 0-79
x_collision=[]
for i in range(79):
    x_collision.append(i+1)
ax1=plt.subplot(211)
ax1.bar(x_collision,result_collision,width=0.5)
ax1.xaxis.set_label_text("channel id")
ax1.yaxis.set_label_text("channel avg collision count")

#第二張圖
# y range - bad channel count
# 將 存放id被占用的次數/48000 算被占用機率
result_probality=[]
for i in result_occpuy:
    result_probality.append(round((i/48000),2))
# initial list
result_badchannel=[]
for i in range(9):
    result_badchannel.append(0)

# 判斷若threshold為0.1~0.9時，是否為bad channel
for i in range(79):

    # for P=0.3 bad channel
    if(i==bad_index): #這個 id channel 不論有無被佔用都是 bad channel
        tmp=math.floor(result_probality[i]*10) # 將機率向上取整 (0.52 --> 5)
        # 將後面沒加到的都加1 
        # (0.52 --> result_badchannel[0~4(host occpuy 加的)][5~8(bad channel加的)])
        for j in range(tmp,8): 
            result_badchannel[j]+=1
    
    # for host occpuy bad channel
    if(result_probality[i]>0.1):
        result_badchannel[0]+=1
    if(result_probality[i]>0.2):
        result_badchannel[1]+=1
    if(result_probality[i]>0.3):
        result_badchannel[2]+=1
    if(result_probality[i]>0.4):
        result_badchannel[3]+=1
    if(result_probality[i]>0.5):
        result_badchannel[4]+=1
    if(result_probality[i]>0.6):
        result_badchannel[5]+=1
    if(result_probality[i]>0.7):
        result_badchannel[6]+=1
    if(result_probality[i]>0.8):
        result_badchannel[7]+=1
    if(result_probality[i]>0.9):
        result_badchannel[8]+=1
# x range
x_probality=[0.1]
for i in range(1,9):
    x_probality.append(x_probality[i-1]+0.1)
ax2=plt.subplot(212)
ax2.bar(x_probality,result_badchannel,width=0.01)
ax2.xaxis.set_label_text("thresold")
ax2.yaxis.set_label_text("bad channel count")

# TODO 畫合併圖
plt.suptitle("host = 70")
plt.show()  
   
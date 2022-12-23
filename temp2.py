import random
import collections
import matplotlib.pyplot as plt


# 前 4secs 的 bad channel probality
# initial
result_occpuy_pre=[] #紀錄占用次數
for i in range(79):
    result_occpuy_pre.append(0)

host_index_pre=[]
host_collision_pre={}
for i in range(6400):
    #print(i)
    host_num_pre=0
    #TODO host num = N
    while(host_num_pre<70):
        channel_index=round((random.randint(1,79)+random.randint(1,79))/2)
        host_index_pre.append(channel_index)
        host_num_pre+=1
    host_collision_pre=collections.Counter(host_index_pre)

    # save and read data
    for key,value in host_collision_pre.items():
        result_occpuy_pre[key-1]=value

result_probality_pre=[] #紀錄占用機率
for i in result_occpuy_pre:
    result_probality_pre.append(round((i/6400),2))

#後 26secs 的 collision probality
# initial
result_collision1=[] #紀錄占用次數
result_collision2=[] 
result_collision3=[] 
result_collision4=[] 
result_collision5=[] 
result_collision6=[] 
result_collision7=[] 
result_collision8=[] 
result_collision9=[]
for i in range(79):
    result_collision1.append(0)
    result_collision2.append(0)
    result_collision3.append(0)
    result_collision4.append(0)
    result_collision5.append(0)
    result_collision6.append(0)
    result_collision7.append(0)
    result_collision8.append(0)
    result_collision9.append(0)

host_index1=[] 
host_index2=[] 
host_index3=[] 
host_index4=[] 
host_index5=[] 
host_index6=[] 
host_index7=[] 
host_index8=[] 
host_index9=[]

host_collision1={}
host_collision2={}
host_collision3={}
host_collision4={}
host_collision5={}
host_collision6={}
host_collision7={}
host_collision8={}
host_collision9={}

good_channel=[]
closest=78
for i in range(41600):
    #print(i)
    host_num=0
    #TODO host num=N
    while(host_num<70):
        #選擇 host 要跳的 channel
        channel_index=random.randint(1,79)

        # -condition1- 如果 threshold>0.1 為 bad channel 跳到另外一個channel
        good_channel.clear()
        closest=78
        #選到 channel 為 bad channel
        if(result_probality_pre[channel_index-1]>0.1):
            #找不是 bad channel 的 (probality<0.1)
            for j in range(len(result_probality_pre)):
                if(result_probality_pre[j]<0.1):
                    good_channel.append(j+1) #紀錄good channel
                    #算離 channel_index 最近的 channel
                    if(closest>abs(j+1-channel_index)):
                        closest=abs(j+1-channel_index)
            
            # 選另外一個channel，如果沒有為原本channel
            if(len(good_channel)!=0):
                # 避免 判斷 index 超標
                tmp=channel_index+closest
                if(tmp>79):
                    tmp=channel_index-closest
                # 距離為正整數，再次判斷是往前還是往後跳躍
                if(result_probality_pre[tmp-1]<0.1):
                    if(channel_index+closest>79):
                        host_index1.append(channel_index-closest)
                    else:
                        host_index1.append(channel_index+closest)
                else:
                    host_index1.append(channel_index-closest)
            else:
                host_index1.append(channel_index)
        else:
            host_index1.append(channel_index)

        # -condition2- 如果 threshold>0.2 為 bad channel 跳到另外一個channel
        good_channel.clear()
        closest=78
        if(result_probality_pre[channel_index-1]>0.2):
            for j in range(len(result_probality_pre)):
                if(result_probality_pre[j]<0.2):
                    good_channel.append(j+1) 
                    if(closest>abs(j+1-channel_index)):
                        closest=abs(j+1-channel_index)
    
            if(len(good_channel)!=0):
                tmp=channel_index+closest
                if(tmp>79):
                    tmp=channel_index-closest
                if(result_probality_pre[tmp-1]<0.2):
                    if(channel_index+closest>79):
                        host_index2.append(channel_index-closest)
                    else:
                        host_index2.append(channel_index+closest)
                else:
                    host_index2.append(channel_index-closest)
            else:
                host_index2.append(channel_index)
        else:
            host_index2.append(channel_index) 

        # -condition3- 如果 threshold>0.3 為 bad channel 跳到另外一個channel
        good_channel.clear()
        closest=78
        if(result_probality_pre[channel_index-1]>0.3):
            for j in range(len(result_probality_pre)):
                if(result_probality_pre[j]<0.3):
                    good_channel.append(j+1) 
                    if(closest>abs(j+1-channel_index)):
                        closest=abs(j+1-channel_index)
    
            if(len(good_channel)!=0):
                tmp=channel_index+closest
                if(tmp>79):
                    tmp=channel_index-closest
                if(result_probality_pre[tmp-1]<0.3):
                    if(channel_index+closest>79):
                        host_index3.append(channel_index-closest)
                    else:
                        host_index3.append(channel_index+closest)
                else:
                    host_index3.append(channel_index-closest)
            else:
                host_index3.append(channel_index)
        else:
            host_index3.append(channel_index)   

        # -condition4- 如果 threshold>0.4 為 bad channel 跳到另外一個channel
        good_channel.clear()
        closest=78
        if(result_probality_pre[channel_index-1]>0.4):
            for j in range(len(result_probality_pre)):
                if(result_probality_pre[j]<0.4):
                    good_channel.append(j+1) 
                    if(closest>abs(j+1-channel_index)):
                        closest=abs(j+1-channel_index)
    
            if(len(good_channel)!=0):
                tmp=channel_index+closest
                if(tmp>79):
                    tmp=channel_index-closest
                if(result_probality_pre[tmp-1]<0.4):
                    if(channel_index+closest>79):
                        host_index4.append(channel_index-closest)
                    else:
                        host_index4.append(channel_index+closest)
                else:
                    host_index4.append(channel_index-closest)
            else:
                host_index4.append(channel_index)
        else:
            host_index4.append(channel_index)   
        
        # -condition5- 如果 threshold>0.5 為 bad channel 跳到另外一個channel
        good_channel.clear()
        closest=78
        if(result_probality_pre[channel_index-1]>0.5):
            for j in range(len(result_probality_pre)):
                if(result_probality_pre[j]<0.5):
                    good_channel.append(j+1) 
                    if(closest>abs(j+1-channel_index)):
                        closest=abs(j+1-channel_index)
    
            if(len(good_channel)!=0):
                tmp=channel_index+closest
                if(tmp>79):
                    tmp=channel_index-closest
                if(result_probality_pre[tmp-1]<0.5):
                    if(channel_index+closest>79):
                        host_index5.append(channel_index-closest)
                    else:
                        host_index5.append(channel_index+closest)
                else:
                    host_index5.append(channel_index-closest)
            else:
                host_index5.append(channel_index)
        else:
            host_index5.append(channel_index)   
        
        # -condition6- 如果 threshold>0.6 為 bad channel 跳到另外一個channel
        good_channel.clear()
        closest=78
        if(result_probality_pre[channel_index-1]>0.6):
            for j in range(len(result_probality_pre)):
                if(result_probality_pre[j]<0.6):
                    good_channel.append(j+1) 
                    if(closest>abs(j+1-channel_index)):
                        closest=abs(j+1-channel_index)
    
            if(len(good_channel)!=0):
                tmp=channel_index+closest
                if(tmp>79):
                    tmp=channel_index-closest
                if(result_probality_pre[tmp-1]<0.6):
                    if(channel_index+closest>79):
                        host_index6.append(channel_index-closest)
                    else:
                        host_index6.append(channel_index+closest)
                else:
                    host_index6.append(channel_index-closest)
            else:
                host_index6.append(channel_index)
        else:
            host_index6.append(channel_index)   
        
        # -condition7- 如果 threshold>0.7 為 bad channel 跳到另外一個channel
        good_channel.clear()
        closest=78
        if(result_probality_pre[channel_index-1]>0.7):
            for j in range(len(result_probality_pre)):
                if(result_probality_pre[j]<0.7):
                    good_channel.append(j+1) 
                    if(closest>abs(j+1-channel_index)):
                        closest=abs(j+1-channel_index)
    
            if(len(good_channel)!=0):
                tmp=channel_index+closest
                if(tmp>79):
                    tmp=channel_index-closest
                if(result_probality_pre[tmp-1]<0.7):
                    if(channel_index+closest>79):
                        host_index7.append(channel_index-closest)
                    else:
                        host_index7.append(channel_index+closest)
                else:
                    host_index7.append(channel_index-closest)
            else:
                host_index7.append(channel_index)
        else:
            host_index7.append(channel_index)   
        
        # -condition8- 如果 threshold>0.8 為 bad channel 跳到另外一個channel
        good_channel.clear()
        closest=78
        if(result_probality_pre[channel_index-1]>0.8):
            for j in range(len(result_probality_pre)):
                if(result_probality_pre[j]<0.8):
                    good_channel.append(j+1) 
                    if(closest>abs(j+1-channel_index)):
                        closest=abs(j+1-channel_index)
    
            if(len(good_channel)!=0):
                tmp=channel_index+closest
                if(tmp>79):
                    tmp=channel_index-closest
                if(result_probality_pre[tmp-1]<0.8):
                    if(channel_index+closest>79):
                        host_index8.append(channel_index-closest)
                    else:
                        host_index8.append(channel_index+closest)
                else:
                    host_index8.append(channel_index-closest)
            else:
                host_index8.append(channel_index)
        else:
            host_index8.append(channel_index)   
        
        # -condition9- 如果 threshold>0.9 為 bad channel 跳到另外一個channel
        good_channel.clear()
        closest=78
        if(result_probality_pre[channel_index-1]>0.9):
            for j in range(len(result_probality_pre)):
                if(result_probality_pre[j]<0.9):
                    good_channel.append(j+1) 
                    if(closest>abs(j+1-channel_index)):
                        closest=abs(j+1-channel_index)
    
            if(len(good_channel)!=0):
                tmp=channel_index+closest
                if(tmp>79):
                    tmp=channel_index-closest
                if(result_probality_pre[tmp-1]<0.9):
                    if(channel_index+closest>79):
                        host_index9.append(channel_index-closest)
                    else:
                        host_index9.append(channel_index+closest)
                else:
                    host_index9.append(channel_index-closest)
            else:
                host_index9.append(channel_index)
        else:
            host_index9.append(channel_index)   
        
        host_num+=1
        
    host_collision1=collections.Counter(host_index1)
    host_collision2=collections.Counter(host_index2)
    host_collision3=collections.Counter(host_index3)
    host_collision4=collections.Counter(host_index4)
    host_collision5=collections.Counter(host_index5)
    host_collision6=collections.Counter(host_index6)
    host_collision7=collections.Counter(host_index7)
    host_collision8=collections.Counter(host_index8)
    host_collision9=collections.Counter(host_index9)

    # save and read data
    for key,value in host_collision1.items():
        if(value>1): # save collision times
            result_collision1[key-1]+=value-1
    
    for key,value in host_collision2.items():
        if(value>1):
            result_collision2[key-1]+=value-1
    
    for key,value in host_collision3.items():
        if(value>1):
            result_collision3[key-1]+=value-1
    
    for key,value in host_collision4.items():
        if(value>1):
            result_collision4[key-1]+=value-1
    
    for key,value in host_collision5.items():
        if(value>1):
            result_collision5[key-1]+=value-1
    
    for key,value in host_collision6.items():
        if(value>1):
            result_collision6[key-1]+=value-1
    
    for key,value in host_collision7.items():
        if(value>1):
            result_collision7[key-1]+=value-1
    
    for key,value in host_collision8.items():
        if(value>1): 
            result_collision8[key-1]+=value-1
    
    for key,value in host_collision9.items():
        if(value>1):
            result_collision9[key-1]+=value-1
    
    host_collision1.clear()
    host_collision2.clear()
    host_collision3.clear()
    host_collision4.clear()
    host_collision5.clear()
    host_collision6.clear()
    host_collision7.clear()
    host_collision8.clear()
    host_collision9.clear()
    
    host_index1.clear()
    host_index2.clear()
    host_index3.clear()
    host_index4.clear()
    host_index5.clear()
    host_index6.clear()
    host_index7.clear()
    host_index8.clear()
    host_index9.clear()


# x range
x=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]


# y range - channel collision probality
y=[]
y.append(sum(result_collision1)/41600/79)
y.append(sum(result_collision2)/41600/79)
y.append(sum(result_collision3)/41600/79)
y.append(sum(result_collision4)/41600/79)
y.append(sum(result_collision5)/41600/79)
y.append(sum(result_collision6)/41600/79)
y.append(sum(result_collision7)/41600/79)
y.append(sum(result_collision8)/41600/79)
y.append(sum(result_collision9)/41600/79)
print(result_probality_pre)
print(y)


plt.bar(x,y,width=0.01)
plt.xlabel("threshold")
plt.ylabel("channel collision probality")
plt.title("host=70") #TODO

plt.show()

  
        
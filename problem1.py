import random
import time
import matplotlib.pyplot as plt

SIM_CNT = 200
HOP_FREQ = 1600

total_time = SIM_CNT * HOP_FREQ #總共跳頻次數
collision = 0 #每次的碰撞次數
total_collision = 0 #總共碰撞次數
prob = 0 #碰撞機率

simulation = [] #存模擬次數
probability = [] #每一次碰撞的機率

for sim in range(SIM_CNT):
    collision = 0
    simulation.append(sim)
    for freq in range(HOP_FREQ):
        device0 = random.randint(1, 80) # 1~79
        device1 = random.randint(1, 80)
        print(device0,"\t",device1)
        #如果挑到的channel一樣，則碰撞+1
        if(device0 == device1):
            collision = collision + 1
            total_collision = total_collision + 1
    probability.append(collision / HOP_FREQ)
    #print("collision:", collision)
    #time.sleep(1)

prob = total_collision / total_time #平均碰撞機率
print("兩個裝置的碰撞機率為：", prob)

plt.bar(simulation, probability)
plt.title("collision simulation of 2 devices") # title
plt.xlabel("simulation count") # x label
plt.ylabel("collision probability") # y label
plt.show()
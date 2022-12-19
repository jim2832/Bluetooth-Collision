import random
import time
import matplotlib.pyplot as plt

SIM_CNT = 30
HOP_FREQ = 1600

collision = 0

device_num = [20, 30, 40, 50, 60, 70]
threshold = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
selected_channel = []

for device in device_num: #device = 20, 30...
    collision = 0
    for dev in range(device): #dev = 1,2,3,4...,20
        selected_channel[dev] = random.randint(1, 79)
    for i in range(1, len(selected_channel)):
        for j in range(i):
            if(selected_channel[i] == selected_channel[j]):
                collision = collision + 1

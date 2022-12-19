import random

all_channel = []
normal_channel = []
interfered_channel = []

#所有channel
for i in range(1, 80):
    all_channel.append(i)
print(all_channel)

#正常的channel
normal_channel = random.sample(range(1, 80), 39)
normal_channel.sort()
print(normal_channel)
print(len(normal_channel))

#被影響的channel
for i in all_channel:
    if i not in normal_channel:
        interfered_channel.append(i)
interfered_channel.sort()
print(interfered_channel)
print(len(interfered_channel))
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


dataname1 = 'results/results_of_emiliotest1_with_haptic_.csv'
dataname2 = 'results/results_of_emiliotest2_with_haptic_.csv'
dataname3 = 'results/results_of_erik3_with_haptic_.csv'
dataname4 = 'results/results_of_erik4_with_haptic_.csv'

# dataname3 = 'results/results_of_Gee_without_haptic_28-Mar-2021_18:22:38.csv'
#
# dataname4 = 'results/results_of_Wil vd Linden_with_haptic_28-Mar-2021_18:17:58.csv'
# dataname5 = 'results/results_of_Gee_with_haptic_28-Mar-2021_18:25:10.csv'
# dataname6 = 'results/results_of_Erik vd Sant_with_haptic_28-Mar-2021_18:32:11.csv'


data2 = pd.read_csv(dataname1)

#plt.plot(data1.values[:,1])

data1 = pd.read_csv(dataname2)

#plt.plot(data2.values[:,1])

data3 = pd.read_csv(dataname3)
data4 = pd.read_csv(dataname4)


print(data1)
ans = pd.DataFrame(data1).to_numpy()
time = ans[:,1]
collide = ans[:,2]
i=0
collision = 0
collision_nr = np.zeros(len(collide))
for col in collide:
    collision += int(col)
    collision_nr[i] = collision
    i +=1
print(collision_nr)
plt.title('collisions')
plt.plot(time,collision_nr)
plt.ylabel('amount of collisions')
plt.xlabel('time [framenumber]')

ans = pd.DataFrame(data2).to_numpy()
time = ans[:,1]
collide = ans[:,2]
i=0
collision = 0
collision_nr = np.zeros(len(collide))
for col in collide:
    collision += int(col)
    collision_nr[i] = collision
    i +=1
print(collision_nr)
plt.title('collisions')
plt.plot(time,collision_nr)
plt.ylabel('amount of collisions')
plt.xlabel('time [framenumber]')

ans = pd.DataFrame(data3).to_numpy()
time = ans[:,1]
collide = ans[:,2]
i=0
collision = 0
collision_nr = np.zeros(len(collide))
for col in collide:
    collision += int(col)
    collision_nr[i] = collision
    i +=1
print(collision_nr)
plt.title('collisions')
plt.plot(time,collision_nr)
plt.ylabel('amount of collisions')
plt.xlabel('time [framenumber]')

ans = pd.DataFrame(data4).to_numpy()
time = ans[:,1]
collide = ans[:,2]
i=0
collision = 0
collision_nr = np.zeros(len(collide))
for col in collide:
    collision += int(col)
    collision_nr[i] = collision
    i +=1
print(collision_nr)
plt.title('collisions')
plt.plot(time,collision_nr)
plt.ylabel('amount of collisions')
plt.xlabel('time [framenumber]')

plt.legend(['#1 training_no_FF','#2 no_FF','#3 training_FF','#4 FF'])
#
# a = np.sum(np.abs(datas[0:1000]))
# b = np.sum(np.abs(datas[1000:2000]))
# c = np.sum(np.abs(datas[2000:3000]))
# d = np.sum(np.abs(datas[3000:4000]))
# e = np.sum(np.abs(datas[4000:5000]))
# f = np.sum(np.abs(datas[5000:6000]))
# mean = np.array([a,b,c,d,e,f])
#
#
# plt.figure()
# plt.plot(mean)
# plt.title('10 sec mean error without haptic shared control')
# plt.ylabel('amount of pixels')
# plt.xlabel('experiment part')
#
# plt.figure()
# ####################
#
# data4 = pd.read_csv(dataname4)
#
# #plt.plot(data1.values[:,1])
#
# data5 = pd.read_csv(dataname5)
#
# #plt.plot(data2.values[:,1])
#
# data6 = pd.read_csv(dataname6)
#
# #plt.plot(data3.values[:,1])
#
# datas = (data4.values[:,2] + data5.values[:,2] +data6.values[:,2])/3
#
#
# plt.plot(datas)
#
#
# plt.title('steering angle without haptic shared control')
# plt.ylabel('degrees')
# plt.xlabel('time [cs]')
#
#
#
#
# a = np.sum(np.abs(datas[0:1000]))
# b = np.sum(np.abs(datas[1000:2000]))
# c = np.sum(np.abs(datas[2000:3000]))
# d = np.sum(np.abs(datas[3000:4000]))
# e = np.sum(np.abs(datas[4000:5000]))
# f = np.sum(np.abs(datas[5000:6000]))
# mean = np.array([a,b,c,d,e,f])
#
#
# plt.figure()
# plt.plot(mean)
#
# plt.title('10 sec mean error with haptic shared control')
# plt.ylabel('amount of pixels')
# plt.xlabel('experiment part')


plt.show()
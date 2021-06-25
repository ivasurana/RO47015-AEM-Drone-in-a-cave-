import pandas as pd
import numpy as np
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt
df = pd.read_csv('map.csv')
rows = len(df.index)
columns = len(df.columns)
tile_size = 16
obstacle_field = np.zeros((tile_size * rows, tile_size * columns))


for index, row in df.iterrows(): #32 itterations (per row)
    for j in range(len(row)):  #length of the row (378 times)  j = element small row
        for i in range(tile_size): #16 itterations per row (per pixel)
            for k in range(tile_size): # 16 itterations per column
                a = j*tile_size+i
                b = index*tile_size+k
                obstacle_field[b,a] = row[j]
                
obstacle_gradient = np.gradient(obstacle_field) #gradient of the obstacle field
force_field = gaussian_filter(obstacle_gradient,sigma=10) #smoothen force feedback field.
force_field = force_field/np.max(force_field) #normalised force function


plt.imshow(force_field[0], cmap=plt.cm.hot, aspect='auto')
plt.colorbar()
plt.figure()
plt.imshow(force_field[1], cmap=plt.cm.hot, aspect='auto')
plt.colorbar()

plt.figure()
plt.imshow(obstacle_field, cmap=plt.cm.hot, aspect='auto')
plt.colorbar()

plt.show()

difference= force_field[0]-force_field[1]
df2 = pd.DataFrame(force_field[0])
df2.to_csv('xtest.csv', index=False, header=False)
df3 = pd.DataFrame(force_field[1])
df3.to_csv('ytest.csv', index=False, header=False)
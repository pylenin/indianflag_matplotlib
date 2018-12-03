"""
Indian National Flag
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patch


#Plotting all the colors of national flag
rect1 = patch.Rectangle((0,0), width=10, height=2, facecolor='g')
rect2 = patch.Rectangle((0,2), width=10, height=2, facecolor='white')
rect3 = patch.Rectangle((0,4), width=10, height=2, facecolor='#FF9933')
fig,ax = plt.subplots()
ax.add_patch(rect1)
ax.add_patch(rect2)
ax.add_patch(rect3)

#Ashok Chakra Circle
r=0.8
plt.plot(5,3, marker = 'o', markerfacecolor = '#000088ff', markersize = 10)
circle1 = plt.Circle((5, 3), r, color='#000088ff', fill=False, linewidth=7)
ax.add_artist(circle1)

#Add small circles inside the edge of circle

small_circles_x = []
small_circles_y = []


for i in range(1,25):
    small_circles_x.append(5+(r-0.05) * np.cos(np.pi/24 + np.pi*i/12))
    small_circles_y.append(3+(r-0.05) * np.sin(np.pi/24 + np.pi*i/12))


plt.plot(small_circles_x, small_circles_y, 'o',
         markersize=4,
         markerfacecolor='#000088ff',
         markeredgecolor = '#000088ff')

#Complete the chakra with 24 spokes
for i in range(0,24):
    x1 =  5 + r/2 * np.cos(np.pi*i/12 + np.pi/48)
    x2 =  5 + r/2 * np.cos(np.pi*i/12 - np.pi/48)
    y1 =  3 + r/2 * np.sin(np.pi*i/12 + np.pi/48)
    y2 =  3 + r/2 * np.sin(np.pi*i/12 - np.pi/48)
    x3 =  5 + r * np.cos(np.pi*i/12)
    y3 =  3 + r * np.sin(np.pi*i/12)
    ax.add_patch(patch.Polygon([[5,3], [x1,y1], [x3,y3],[x2,y2]], fill=True, closed=True, color='#000088ff'))


plt.axis('equal')
plt.show()
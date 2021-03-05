# ----------------------------------------------------------------
#   demonstrate loading and visualizing polygons using matploblib
#   
#   (C) 2021 Stephen Ellias, New York, USA
#   Released under GNU Public License (GPL)
#   Refer to github.com/sellias
# ----------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as a3

# prepare figure size, add 3D axes, set viewing distance, set limits, set labels
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([0,5])
ax.set_ylim([0,5])
ax.set_zlim([0,5])

# prepare a demo triangle, cyan body, black edge, add to axes
vtx = [2,2,0], [2,1,3], [4,4,5]
tri = a3.art3d.Poly3DCollection([vtx])
tri.set_color('c')
tri.set_edgecolor('k')
ax.add_collection3d(tri)

# use interactive mode
plt.ion()
plt.draw()

# display rotating view forever
while True:
    for angle in range(360):
        # set view angle, view distance, show, and pause
        ax.view_init(20, angle)
        ax.dist = 9
        plt.draw()
        plt.pause(.001)
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

def main():
    plot_init()
    plot_demo_one()
    plot_show_still()

def plot_init():
    """prepare figure, 3D axes, size, range, viewing distance, labels"""
    global fig, ax, plot_view_dist
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, projection='3d')
    plot_view_dist = 9
    ax.set_xlim([0,5])
    ax.set_ylim([0,5])
    ax.set_zlim([0,5])
    plt.ion()
    return()

def plot_demo_one():
    """prepare a demo triangle, plot on axes, draw plot"""
    vtx = [2,2,0], [2,1,3], [4,4,5]
    tri = a3.art3d.Poly3DCollection([vtx])
    tri.set_color('c')
    tri.set_edgecolor('k')
    ax.add_collection3d(tri)

def plot_show_still():
    plt.show(block=True)

def plot_show_rotating():
    """rotate a 3D plot, set range, speed multiplyer"""
    while True:
        for angle in range(360):
            # set view angle, view distance, show, and pause
            ax.view_init(20, angle)
            ax.dist = plot_view_dist
            plt.draw()
            plt.pause(.001)

if __name__ == '__main__':
    main()
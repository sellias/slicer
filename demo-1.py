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
    plot_show_rotating()

def plot_init():
    """prepare figure, 3D axes, size, range, viewing distance, labels"""
    global fig, ax, plot_view_dist
    fig = plt.figure(figsize=(12,12))
    ax = fig.add_subplot(111, projection='3d')
    plot_view_dist = 9
    ax.set_xlim([0,5])
    ax.set_ylim([0,5])
    ax.set_zlim([0,5])
    plt.ion()
    return()

def plot_demo_one():
    """prepare a demo triangle, demo plane, plot on axes, draw plot"""
    # segment
    seg_vtx = [3,3,2.5], [2,1.2,2.5]
    seg = a3.art3d.Line3DCollection([seg_vtx])
    seg.set_edgecolor('black')
    seg.set_linewidth(4)
    ax.add_collection3d(seg)
    # triangle
    tri_vtx = [2,2,0], [2,1,3], [4,4,5]
    tri = a3.art3d.Poly3DCollection([tri_vtx])
    tri = a3.art3d.Poly3DCollection([tri_vtx])
    tri.set_edgecolor('blue')
    tri.set_color((0, 0.5, 1, 0.4))
    tri.set_linewidth(2)
    ax.add_collection3d(tri)
    # plane
    plane_vtx = [0,0,2.5], [0,5,2.5], [5,5,2.5], [5,0,2.5]
    plane = a3.art3d.Poly3DCollection([plane_vtx])
    plane.set_color((1, 0, 0, 0.1))
    ax.add_collection3d(plane)

def plot_show_still():
    plt.show(block=True)

def plot_show_rotating():
    """rotate a 3D plot, set range, speed multiplyer"""
    while True:
        for angle in range(360):
            # set view angle, view distance, show, and pause
            ax.view_init(15, angle)
            ax.dist = plot_view_dist
            plt.draw()
            plt.pause(.001)

if __name__ == '__main__':
    main()
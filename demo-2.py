#!/bin/python
# ----------------------------------------------------------------
#   
#   
#   (C) 2021 Stephen Ellias, New York, USA
#   Released under GNU Public License (GPL)
#   Refer to github.com/sellias
# ----------------------------------------------------------------

import matplotlib.pyplot as plt

class Plotter:
    """A sample example plotter"""

    def __init__(self):
        self.fig = plt.figure(figsize=(6,6))
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.view_dist = 9
        self.xlim = 5
        self.ylim = 5
        self.zlim = 5
    
    def set_limits(self, ixlim, iylim, izlim):
        self.ax.set_xlim(ixlim)
        self.ax.set_ylim(iylim)
        self.ax.set_zlim(izlim)



#!/bin/python
# ----------------------------------------------------------------
#   geometry class file
#       for the handling of stl geometry
#       importing, parsing, basic stats
#       returns list of triangles as three
#       sets of 3d vectors
#   
#   (c) 2021 stephen ellias, new york, usa
#   released under gnu public license (gpl)
#   refer to github.com/sellias
# ----------------------------------------------------------------

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from stl import mesh
import numpy as np
import sys

class STLGeometry:
    #-----------------------------------------
    #       for the handling of stl geometry
    #       importing, parsing, basic stats
    #       returns list of triangles as three
    #       sets of 3d vectors
    #-----------------------------------------
    """"""
    VERBOSE = True
    mesh = None
    """derived stats"""
    dimensions = None
    range = None
    faces = None
    x_min = None
    x_max = None
    y_min = None
    y_max = None
    z_min = None
    z_max = None

    def __init__(self, stl_filepath):
        """   initialize STLGeometry using imported data from an .stl file   """
        if self.VERBOSE : print("Importing STL File:" ,stl_filepath)
        try:
            self.mesh = mesh.Mesh.from_file(stl_filepath)
        except FileNotFoundError:
            # TODO check if this works
            raise RuntimeError("file not found: ,",stl_filepath)
        
        self.derive_statistics()

    def derive_statistics(self):
        # TODO finish all stats
        """major stats"""
        self.faces = self.mesh.vectors.size
        self.dimensions = [self.x_max-self.x_min, self.y_max-self.y_min, self.z_max-self.z_min]
        """boundaries"""
        self.x_max = np.max(self.mesh.vectors[:,:,0])
        self.x_min = np.min(self.mesh.vectors[:,:,0])
        self.y_max = np.max(self.mesh.vectors[:,:,1])
        self.y_min = np.min(self.mesh.vectors[:,:,1])
        self.z_max = np.max(self.mesh.vectors[:,:,2])
        self.z_min = np.min(self.mesh.vectors[:,:,2])

    def print_stats(self):
        """size, triangle count, file name, range"""
        print(f'Geometry Statistics:')
        print(f'\tSize:   \t {self.dimensions[0]:.0f}mm x {self.dimensions[1]:.0f}mm x {self.dimensions[2]:.0f}mm')
        print(f'\tFace Count:\t {self.faces:,}')
        print(f'\tX Range:\t {self.x_min:.3f}, {self.x_max:.3f}')
        print(f'\tY Range:\t {self.y_min:.3f}, {self.y_max:.3f}')
        print(f'\tZ Range:\t {self.z_min:.3f}, {self.z_max:.3f}')

def main():
    """import stl file"""
    geometry = STLGeometry("/home/stephen/projects/slicer/3DBenchy.stl")
    """display stats"""
    geometry.print_stats()

if __name__ == '__main__':
    main()
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
    filepath = None
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


    def __init__(self, ifilepath):
        self.filepath = ifilepath
        # TODO test new constructor
        """Load in geometry from an stl file"""        
        try:
            self.mesh = mesh.Mesh.from_file(self.filepath)
        except FileNotFoundError:
            print("file not found: ,",self.filepath) 
        
        self.derive_statistics()

    def derive_statistics(self):
        # TODO finish all stats
        """boundaries"""
        self.x_max = np.max(self.mesh.vectors[:,:,0])
        self.x_min = np.min(self.mesh.vectors[:,:,0])
        self.y_max = np.max(self.mesh.vectors[:,:,1])
        self.y_min = np.min(self.mesh.vectors[:,:,1])
        self.z_max = np.max(self.mesh.vectors[:,:,2])
        self.z_min = np.min(self.mesh.vectors[:,:,2])
        """major stats"""
        self.faces = self.mesh.vectors.size
        self.dimensions = [
            self.x_max-self.x_min,
            self.y_max-self.y_min,
            self.z_max-self.z_min
            ]
        self.range = [
            self.x_min, self.x_max,
            self.y_min, self.y_max,
            self.z_min, self.z_max,
        ]

    def print_stats(self):
        """size, triangle count, file name, range"""
        print(f'Geometry Statistics:')
        print(f'\tFilepath:\t {self.filepath}')
        print(f'\tSize:    \t {self.dimensions[0]:.0f}mm x {self.dimensions[1]:.0f}mm x {self.dimensions[2]:.0f}mm')
        print(f'\tX Range: \t {self.x_min:.3f}, {self.x_max:.3f}')
        print(f'\tY Range: \t {self.y_min:.3f}, {self.y_max:.3f}')
        print(f'\tZ Range: \t {self.z_min:.3f}, {self.z_max:.3f}')
        print(f'\tFaces:   \t {self.faces:,}')
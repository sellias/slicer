#!/bin/python
# ----------------------------------------------------------------
#   cli based slicer implementation
#       -import stl
#       -draw first sigure for visualize stl geometry
#       -draw second placeholder figure for triangle plane intersection
#       -draw third placeholder figure for intersection profile
#       -visualize intersection planes
#       -highlight plane intersecting triangles
#       -visualize triangle plane, line-plane intersections
#       -visualize intersection profile
#       -automate, animate, and label for all planes based on layer height
#   
#   (c) 2021 stephen ellias, new york, usa
#   released under gnu public license (gpl)
#   refer to github.com/sellias
# ----------------------------------------------------------------

import sys, os
from STLGeometry import STLGeometry as STL

def main():
    """validate input arguments"""
    if len(sys.argv) != 2:
        print('ERROR: please provide target filename')
        exit()
    if not os.path.exists(sys.argv[1]):
        print('ERROR: file not found')
        exit()

    """import the stl geometry"""
    print('Importing \'', sys.argv[1], '\'')
    obj = STL(sys.argv[1])

    """print geometry statistics"""
    obj.print_stats()

if __name__ == '__main__':
    main()
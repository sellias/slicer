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
    print("")
    # import and validate stl file
    validateArgs()
    obj = STL(sys.argv[1])

    obj.print_stats()

def validateArgs():
    """validate input arguments"""
    if len(sys.argv) != 2:
        print('ERROR: please provide target filename')
        exit()
    if not os.path.exists(sys.argv[1]):
        print('ERROR: file not found')
        exit()

if __name__ == '__main__':
    main()
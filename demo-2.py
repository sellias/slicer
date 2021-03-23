#!/bin/python
# ----------------------------------------------------------------
#   demo 2
#       > import stl file
#       > visualize data  
#   
#   (c) 2021 stephen ellias, new york, usa
#   released under gnu public license (gpl)
#   refer to github.com/sellias
# ----------------------------------------------------------------

# import enum
import warnings
from numpy.core.fromnumeric import amax
warnings.simplefilter(action='ignore', category=FutureWarning)
from stl import mesh
import numpy as np

def main():
    # test variables
    TEST_STL_1 = "/home/stephen/projects/slicer/3DBenchy.stl"

    # import an stl file
    obj = mesh.Mesh.from_file(TEST_STL_1)

    # # display stats on sample triangle
    # i = 10_000
    # print(f'geometry[{i}]:\n{geometry.vectors[i]}\n')
    # # display segments from triangle
    # print(f'geometry[{i}] segments:')
    # print(f'{geometry.vectors[i][0]} -> {geometry.vectors[i][1]}')
    # print(f'{geometry.vectors[i][1]} -> {geometry.vectors[i][2]}')
    # print(f'{geometry.vectors[i][2]} -> {geometry.vectors[i][0]}\n')

    # for i, tri in enumerate(geometry.vectors):
    #     print(f'{i}\n{tri}\n')

    t_obj = obj.vectors
    # t_obj = obj.vectors[10_000:10_004]
    c = 0
    for i, tri in enumerate(t_obj):
        # print(f'{i}:\nX: {tri[:, 0]}\nY: {tri[:, 1]}\nZ: {tri[:, 2]}')
        c = i
    print(f'Count: {c}')
    print(f'Geometry Statistics:')
    print(f'All X Values:\n\t{t_obj[:,:,0]}')
    print(f'All Y Values:\n\t{t_obj[:,:,1]}')
    print(f'All Z Values:\n\t{t_obj[:,:,2]}')
    print(f'Max X Value:\t{np.max(t_obj[:,:,0])}') 
    print(f'Min X Value:\t{np.min(t_obj[:,:,0])}')  
    print(f'Max Y Value:\t{np.max(t_obj[:,:,1])}') 
    print(f'Min Y Value:\t{np.min(t_obj[:,:,1])}')  
    print(f'Max Z Value:\t{np.max(t_obj[:,:,2])}') 
    print(f'Min Z Value:\t{np.min(t_obj[:,:,2])}')
    x_size = round(np.max(t_obj[:,:,0]) - np.min(t_obj[:,:,0]), 3)
    y_size = round(np.max(t_obj[:,:,1]) - np.min(t_obj[:,:,1]), 3)
    z_size = round(np.max(t_obj[:,:,2]) - np.min(t_obj[:,:,2]), 3)
    # x_size = round(x_size, 3)
    print(f'Size:\t\t%.0fmm x %.0fmm x %.0fmm' % (x_size, y_size, z_size))  

if __name__ == '__main__':
    main()
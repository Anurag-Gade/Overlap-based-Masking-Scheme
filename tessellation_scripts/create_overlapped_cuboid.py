import numpy as np
from check_coordinate import *

def create_cuboid(start_dict, end_dict, shape):
    
    the_cube = np.zeros(shape=shape) 
    
    # X Coordinates
    for i in range(shape[0]):
        
        # Y Coordinates
        for j in range(shape[1]):
            
            #Z Coordinates
            for k in range(shape[2]):
                
                coordinate = [i, j, k]
                result = check_coordinate_subcuboid(coordinate, start_dict, end_dict)
                
                value = 0
                for key in range(1,len(result)+1):
                    
                    if(int(result[key]) == 1):
                        
                        value += key
                
                the_cube[i,j,k] = value
                
    
    return the_cube                

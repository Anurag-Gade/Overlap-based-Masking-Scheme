def add_overlaps(adjacency_dict, start_dict, end_dict):
    
    
    '''
    Logic of this function is as follows:
     - Will be reading the sub cuboids, adjacency dictionary, start coordinate dictionary, 
       and the end coordinate dictionary. 
     - For every key in the adjacency dictionary, read the end coordinates of that particular key. 
     - For each value corresponding to that particular key, the start coordinate corresponding to the
       value will be compared to the end coordinate of the value. We see if the difference of the 
       subtraction along any of the 3 axis equals 8. If it does, the overlapping exists in that direction 
       and we sum the values of the sub-cubes in that particular axis. 
     - Alternatively, we can devise an approach which uses the ending coordinates. We see which of the one
       coordinate differs from one another and subtract the offsets from the intersecting regions.
    '''
    
    sub_cuboids = np.zeros(shape=(128,128,90))
    overlapping_factor = 8
    for key in adjacency_dict:

        for i in range(len(adjacency_dict[key])):

            adjacent_cube_index = adjacency_dict[key][i]
            print("Cube {adjacent_cube_num} is adjacent to Cube {key}".format(adjacent_cube_num=adjacent_cube_index, key=key))

            counter = 0
            for dim in range(3):
                if(end_dict[adjacent_cube_index][dim] != end_dict[key][dim]): 
                    print(f"Dimension along which overlapping is required is {dim}")
                    counter = counter + dim

            pre_val_x = start_dict[key][0]
            pre_val_y = start_dict[key][1]
            pre_val_z = start_dict[key][2]
            
            end_pre_val_x = end_dict[key][0]
            end_pre_val_y = end_dict[key][1]
            end_pre_val_z = end_dict[key][2] 

            pre_val_sec_x = start_dict[adjacent_cube_index][0]
            pre_val_sec_y = start_dict[adjacent_cube_index][1]
            pre_val_sec_z = start_dict[adjacent_cube_index][2]
            
            end_pre_val_sec_x = end_dict[adjacent_cube_index][0]
            end_pre_val_sec_y = end_dict[adjacent_cube_index][1]
            end_pre_val_sec_z = end_dict[adjacent_cube_index][2]

            print(key + adjacent_cube_index) 
            
            print(counter)
            if(counter == 0):
                sub_cuboids[end_pre_val_x - overlapping_factor:end_pre_val_x, pre_val_y:end_pre_val_y - overlapping_factor, pre_val_z:end_pre_val_z - overlapping_factor] = key + adjacent_cube_index
                
            if(counter == 1):
                sub_cuboids[pre_val_x:end_pre_val_x - overlapping_factor, end_pre_val_y - overlapping_factor:end_pre_val_y, pre_val_z:end_pre_val_z - overlapping_factor] = key + adjacent_cube_index

            if(counter == 2):
                sub_cuboids[pre_val_x:end_pre_val_x - overlapping_factor, pre_val_y:end_pre_val_y - overlapping_factor, end_pre_val_z - overlapping_factor:end_pre_val_z] = key + adjacent_cube_index


            counter = 0 #Counter Reset

    return sub_cuboids

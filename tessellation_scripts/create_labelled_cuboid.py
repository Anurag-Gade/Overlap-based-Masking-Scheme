def create_labelled_cuboid(shape, start_dict, end_dict):
    
    labelled_cuboid = np.zeros((128,128,90)) 
    
    #Below "key" denotes the cuboid number
    for key in range(1,len(start_dict)+1):
        
        start_coords = start_dict[key]
        
        print(start_coords)
        end_coords = end_dict[key] 
        print(end_coords)
        labelled_cuboid[start_coords[0]:end_coords[0], start_coords[1]:end_coords[1], start_coords[2]:end_coords[2]] = key
        
    return labelled_cuboid

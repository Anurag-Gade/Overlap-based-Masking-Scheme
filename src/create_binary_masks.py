def create_binary_mask(start_dict, end_dict, shape):
    
    masks = []
    for key in start_dict:
        blank_array = np.zeros(shape=shape) 
        
        blank_array[start_dict[key][0]:end_dict[key][0], start_dict[key][1]:end_dict[key][1], start_dict[key][2]:end_dict[key][2]] = 1
        masks.append(blank_array) 
    
    return masks

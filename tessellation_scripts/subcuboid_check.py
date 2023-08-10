def check_coordinate_subcuboid(coord, start_dict, end_dict):
    result = {}
    
    for subcuboid in start_dict.keys():
        start_coord = start_dict[subcuboid]
        end_coord = end_dict[subcuboid]
        
        is_inside = all(start <= c <= end for c, start, end in zip(coord, start_coord, end_coord))
        result[subcuboid] = is_inside
    
    return result

import numpy as np

def divide_cuboid(cuboid, overlap, num_sub_cuboids_dim):
    # Calculate the number of sub-cuboids in each dimension
#     num_sub_cuboids_per_dim = int(round(total_num_sub_cuboids ** (1/3)))
#     print(num_sub_cuboids_per_dim)
    # Get the dimensions of the cuboid
    cuboid_shape = cuboid.shape
    
    overlap = int(overlap/2)
    
    num_sub_cuboids_x = num_sub_cuboids_dim['num_sub_cuboids_x']
    num_sub_cuboids_y = num_sub_cuboids_dim['num_sub_cuboids_y']
    num_sub_cuboids_z = num_sub_cuboids_dim['num_sub_cuboids_z']
    
    
    # Calculate the size of each sub-cuboid without considering the overlap
#     sub_cuboid_size = [dim // num_sub for dim, num_sub in zip(cuboid_shape, [num_sub_cuboids_per_dim] * 3)]
#     print(sub_cuboid_size)
#     print(sub_cuboid_size) 
    original_x = cuboid_shape[0] // num_sub_cuboids_x
    original_y = cuboid_shape[1] // num_sub_cuboids_y
    original_z = cuboid_shape[2] // num_sub_cuboids_z
    
    sub_cuboid_size = [original_x, original_y, original_z]
    print(sub_cuboid_size)
    
    sub_cuboids = []
    start_coords = []
    end_coords = [] 
    
    cube_num = 1
    # Generate the sub-cuboids
    for i in range(num_sub_cuboids_x):
        for j in range(num_sub_cuboids_y):
            for k in range(num_sub_cuboids_z):
                if(i == 0 and j == 0 and k == 0):
                    sub_cuboid_start = [i * sub_cuboid_size[0],
                                        j * sub_cuboid_size[1],
                                        k * sub_cuboid_size[2]]
                else:
                    sub_cuboid_start = [i * sub_cuboid_size[0] - overlap,
                                        j * sub_cuboid_size[1] - overlap,
                                        k * sub_cuboid_size[2] - overlap]
                if(sub_cuboid_start[0]<0):
                    sub_cuboid_start[0] += overlap
                if(sub_cuboid_start[1]<0):
                    sub_cuboid_start[1] += overlap
                if(sub_cuboid_start[2]<0):
                    sub_cuboid_start[2] += overlap
                    
                start_coords.append(sub_cuboid_start)  
                start_coord = start_coords[cube_num-1]
                
                sub_cuboid_end = [start_coord[0] + sub_cuboid_size[0] + overlap,
                                  start_coord[1] + sub_cuboid_size[1] + overlap,
                                  start_coord[2] + sub_cuboid_size[2] + overlap]
                if(sub_cuboid_end[0]>cuboid_shape[0]):
                    sub_cuboid_end[0] = sub_cuboid_end[0]-overlap
                if(sub_cuboid_end[1]>cuboid_shape[1]):
                    sub_cuboid_end[1] = sub_cuboid_end[1]-overlap
                if(sub_cuboid_end[2]>cuboid_shape[2]):
                    sub_cuboid_end[2] = sub_cuboid_end[2]-overlap
                end_coords.append(sub_cuboid_end) 
                sub_cuboid_slices = [slice(sub_cuboid_start[dim], sub_cuboid_end[dim]) for dim in range(3)]
                sub_cuboid_data = cuboid[tuple(sub_cuboid_slices)]
                
                masked_data = np.full(sub_cuboid_data.shape,cube_num)
                sub_cuboids.append(masked_data)
                cube_num += 1 

    return sub_cuboids, start_coords, end_coords


# Example usage:
# Replace 'cuboid_data' with the actual 3D cuboid data (a 3D NumPy array)
cuboid_data = np.random.rand(132,132,90)  # Replace this with your cuboid data
# total_num_sub_cuboids = 12  # Replace with the total number of sub-cuboids you want
overlap = 8  # Replace with the desired overlap (integer)
# num_sub_cubes_depth = 2  # Replace with the number of sub-cubes along the depth dimension (integer)
num_sub_cuboids_dim = {'num_sub_cuboids_x':3,
                      'num_sub_cuboids_y':2,
                      'num_sub_cuboids_z':2}


sub_cuboids, start_coords, end_coords = divide_cuboid(cuboid_data, overlap, num_sub_cuboids_dim)
for i, sub_cuboid in enumerate(sub_cuboids):
    print(f"Sub-cuboid {i + 1}: Shape: {sub_cuboid.shape}")
# print(sub_cuboids[3])
for i, start_coord in enumerate(start_coords):
    print(f"Sub-cuboid {i+1}: Start Coordinates: {start_coord}") 

for i, end_coord in enumerate(end_coords):
    print(f"Sub-cuboid {i+1}: End Coordinates: {end_coord}")

import numpy as np
import nibabel as nib
from overlapping_coordinates import *
from conv2dict import *
from adjacency_check import *
from create_overlapped_cuboid import *
from create_binary_masks import *
from segregate_masks import *

import argparse
import os

parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter, description = "Overlap-based Masking Scheme")

parser.add_argument('--input_path', action='store', required=True,
                    type=str, help='Path to a 3-dimensional input file (.nii)') 

parser.add_argument('--out_folder', action='store', required=True,
                    type=str, help='Path to output folder which stores the masks')

# parser.add_argument('--volume_shape', action='store', required=True,
#                    type=str, help='Shape of the volume intended to mask') 

parser.add_argument('--sub_cuboids_along_x', action='store', default=2, 
                    type=int, help='Number of sub-cuboids along x axis')

parser.add_argument('--sub_cuboids_along_y', action='store', default=2,
                    type=int, help='Number of sub-cuboids along y axis')

parser.add_argument('--sub_cuboids_along_z', action='store', default=2,
                    type=int, help='Number of sub-cuboids along z axis') 

parser.add_argument('--overlap', action='store', default=8, 
                    type=int, help='Overlapping factor') 

parser.add_argument('--segregate', action='store', default=False,
                    type=bool, help='Boolean flag to activate segregation of the overlapping masks')


args = parser.parse_args() 

input_path = args.input_path
out_folder = args.out_folder
sub_cuboids_along_x = args.sub_cuboids_along_x
sub_cuboids_along_y = args.sub_cuboids_along_y
sub_cuboids_along_z = args.sub_cuboids_along_z
overlap = args.overlap
segregate = args.segregate

input_nii = nib.load(input_path)
input_nii_arr = input_nii.get_fdata() 

#Input Dimensions
x_dim = input_nii_arr.shape[0]
y_dim = input_nii_arr.shape[1]
z_dim = input_nii_arr.shape[2]

cuboid_data = np.random.rand(x_dim, y_dim, z_dim)  # Replace this with your cuboid data
# total_num_sub_cuboids = 4  # Replace with the total number of sub-cuboids you want
overlap = overlap  # Replace with the desired overlap (integer)
num_sub_cuboids_dim = {"num_sub_cuboids_x":sub_cuboids_along_x,  # Replace with the number of sub-cubes along the depth dimension (integer)
                   "num_sub_cuboids_y":sub_cuboids_along_y,
                   "num_sub_cuboids_z":sub_cuboids_along_z}


sub_cuboids, start_coords, end_coords = divide_cuboid(cuboid_data, overlap, num_sub_cuboids_dim)

for i, sub_cuboid in enumerate(sub_cuboids):
    print(f"Sub-cuboid {i + 1}: Shape: {sub_cuboid.shape}")
# print(sub_cuboids[3])
for i, start_coord in enumerate(start_coords):
    print(f"Sub-cuboid {i+1}: Start Coordinates: {start_coord}")

for i, end_coord in enumerate(end_coords):
    print(f"Sub-cuboid {i+1}: End Coordinates: {end_coord}")

start_dict = conv_to_dict(start_coords)
end_dict = conv_to_dict(end_coords)

adjacency_dict = check_for_adjacency(start_dict)

#Path to save the NumPy array
array_path = os.path.join(out_folder, "output_cuboid.npy")
#Path to save the NIfTI output
nifti_path = os.path.join(out_folder, "output_cuboid.nii.gz")
#Path to save the binary mask
binary_mask_array_path = os.path.join(out_folder, "binary_mask.npy")
#Path to save the binary mask (NIfTI)
binary_mask_nifti_path = os.path.join(out_folder, "binary_mask.nii.gz") 

generated_cuboid = create_cuboid(start_dict, end_dict, (x_dim, y_dim, z_dim))
np.save(array_path, generated_cuboid)

print("Numpy File Saved")

nii_file = nib.Nifti1Image(generated_cuboid, affine=np.eye(4))
nib.save(nii_file, nifti_path)

print("NIfTI File Saved")

#Generate Masks

masks = create_binary_mask(start_dict, end_dict, (x_dim, y_dim, z_dim))
np.save(binary_mask_array_path, masks)

binary_mask_nii = nib.Nifti1Image(masks, affine=np.eye(4))
nib.save(binary_mask_nifti_path, binary_mask_nii) 

print("Masks Saved")

if segregate:

    ROOT_DIR = out_folder + "segregated_masks"

    if os.path.isdir(ROOT_DIR):
        os.mkdir(ROOT_DIR) 
        
    masks_path = binary_mask_array_path
  
    segregate_masks(ROOT_DIR, masks_path)

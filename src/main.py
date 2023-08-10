import numpy as np
import nibabel as nib
from overlapping_coordinates import *
from conv2dict import *
from adjacency_check import *
from create_overlapped_cuboid import *

cuboid_data = np.random.rand(128,128,90)  # Replace this with your cuboid data
total_num_sub_cuboids = 4  # Replace with the total number of sub-cuboids you want
overlap = 8  # Replace with the desired overlap (integer)
num_sub_cubes_depth = 2  # Replace with the number of sub-cubes along the depth dimension (integer)

sub_cuboids, start_coords, end_coords = divide_cuboid(cuboid_data, total_num_sub_cuboids, overlap, num_sub_cubes_depth)

start_dict = conv_to_dict(start_coords)
end_dict = conv_to_dict(end_coords) 

adjacency_dict = check_for_adjacency(start_dict)

cube = create_cuboid(start_dict, end_dict, (128,128,90))

np.save("D:/Research/Harvard/OverlappingTesselations/outputs/verification_outputs/cube_1.npy", cube)

print("Numpy File Saved")

nii_file = nib.Nifti1Image(cube, affine=np.eye(4))

nib.save(nii_file, "D:/Research/Harvard/OverlappingTesselations/outputs/nifti_outputs/cube_1.nii")

print("NIfTI File Saved")

import numpy as np
import nibabel as nib
from overlapping_coordinates import *
from conv2dict import *
from adjacency_check import *
from create_overlapped_cuboid import *
from create_binary_masks import *
from segregate_masks import *
import argparse

parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter, description = "Overlap-based Masking Scheme")

parser.add_argument("--volume_shape", action='store', required=True,
                   type=str, help='Shape of the volume intended to mask') 


cuboid_data = np.random.rand(145, 174, 145)  # Replace this with your cuboid data
# total_num_sub_cuboids = 4  # Replace with the total number of sub-cuboids you want
overlap = 8  # Replace with the desired overlap (integer)
num_sub_cuboids_dim = {"num_sub_cuboids_x":5,  # Replace with the number of sub-cubes along the depth dimension (integer)
                   "num_sub_cuboids_y":6,
                   "num_sub_cuboids_z":5}


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

cube = create_cuboid(start_dict, end_dict, (145, 174, 145))

np.save("/data/pnl/home/ag1666/coeff_dir/CuboidTesselation/outputs/verification_outputs/cube_1.npy", cube)

print("Numpy File Saved")

nii_file = nib.Nifti1Image(cube, affine=np.eye(4))

nib.save(nii_file, "/data/pnl/home/ag1666/coeff_dir/CuboidTesselation/outputs/nifti_outputs/cube_1.nii")

print("NIfTI File Saved")

#Generate Masks

masks = create_binary_mask(start_dict, end_dict, (145, 174, 145))
np.save("/data/pnl/home/ag1666/coeff_dir/CuboidTesselation/outputs/verification_outputs/masks_1.npy", masks)

print("Masks Saved")

ROOT_DIR = "/data/pnl/home/ag1666/coeff_dir/CuboidTesselation/outputs/verification_outputs"

masks_path = os.path.join(ROOT_DIR, "masks_1.npy")

segregate_masks(ROOT_DIR, masks_path)

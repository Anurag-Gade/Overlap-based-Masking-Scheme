# Overlap-based Masking Scheme

Masking schemes tend to be vital in various computer vision tasks, for the purpose of marking a particular region of interest we intend the algorithm to act upon. Here, we propose a labelled and a binary cuboidal masking scheme with the option of providing an overlapping factor for the sub-cuboids.  

```
>>> python main.py --input_path <path_to_the_volume (str)> --out_folder <path_to_output_folder (str)> --sub_cuboids_along_x <optional (int), number of sub-cuboids along x-axis> --sub_cuboids_along_y <optional (int), number of sub-cuboids along y-axis> --sub_cuboids_along_z <optional (int), number of sub-cuboids along z-axis> --overlap <overlapping factor (int), which is the size of overlap for each sub-cuboid> --segregate <True or False (bool), based on input the binary mask will be segregated into its consitutents and saved in a sub-directory in the output folder>
```

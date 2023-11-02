# Overlap-based Masking Scheme

Masking schemes tend to be vital in various computer vision tasks, for the purpose of marking a particular region of interest we intend the algorithm to act upon. Here, we propose a labelled and a binary cuboidal masking scheme with the option of providing an overlapping factor for the sub-cuboids.  


Below is an example of the terminal input;
```
>>> python main.py --input_path <str> --out_folder <str> --sub_cuboids_along_x <int> --sub_cuboids_along_y <int> --sub_cuboids_along_z <int> --overlap <int> --segregate <bool>
```

Arguments:

* input_path (type:str) -- The absolute path to the volume file intended to mask should be provided in this argument.
* out_folder (type:str) -- The absolute path to the directory in which the outputs are to be saved.
* sub_cuboids_along_x (type:int, optional, default:2) -- The number of sub-cuboids the overall volume needs to be partitioned into along the x-axis.
* sub_cuboids_along_y (type:int, optional, default:2) -- The number of sub-cuboids the overall volume needs to be partitioned into along the y-axis.
* sub_cuboids_along_z (type:int, optional, default:2) -- The number of sub-cuboids the overall volume needs to be partitioned into along the z-axis.
* overlap (type:int, optional, default:8) -- The overlapping factor by which each sub-cuboid will overlap with its adjacent partitions.
* segregate (type:bool, optional, default:False) -- Flag to enable segregation in the script, if enabled the binary mask is segregated into its constituent sub-cuboids and saved in seperate folders.


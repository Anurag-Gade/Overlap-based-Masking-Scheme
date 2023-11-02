#! /bin/bash 

# Can place in a for loop in case of multiple inputs. However, double-check the input and output directories so that the outputs will not be overwritten by subsequent outputs generated.
python main.py --input_path <str> --out_folder <str> --sub_cuboids_along_x <int> --sub_cuboids_along_y <int> --sub_cuboids_along_z <int> --overlap <int> --segregate <bool>

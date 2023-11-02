# Overlap-based Masking Scheme

Masking schemes tend to be vital in various computer vision tasks, for the purpose of marking a particular region of interest we intend the algorithm to act upon. Here, we propose a labelled and a binary cuboidal masking scheme with the option of providing an overlapping factor for the sub-cuboids.  

```
>>> python main.py --input_path <str> --out_folder <str> --sub_cuboids_along_x <int> --sub_cuboids_along_y <int> --sub_cuboids_along_z <int> --overlap <int> --segregate <bool>
```

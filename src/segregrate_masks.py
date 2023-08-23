#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:55:19 2023

@author: ag1666
"""

import numpy as np
import nibabel as nib
import os

ROOT_DIR = "/data/pnl/home/ag1666/coeff_dir/CuboidTesselation/outputs/verification_outputs"

masks_path = os.path.join(ROOT_DIR, "masks_1.npy")

def segregate_masks(ROOT_DIR, masks_path):
      
      consolidated_masks = np.load(masks_path)

      print(consolidated_masks.shape)

      total_masks = consolidated_masks.shape[0]

      SUB_ROOT_DIR = os.path.join(ROOT_DIR, "masks_folder")
      
      if(os.path.isdir(SUB_ROOT_DIR)
      os.mkdir(SUB_ROOT_DIR)

      for i in range(total_masks):
          
          print("Mask Number: {num}".format(num = i+1))
          name = "mask_{mask_num}".format(mask_num = i+1)
          
          folder_path = os.path.join(SUB_ROOT_DIR, name)
          os.mkdir(folder_path)
          
          file_name = "mask_{mask_no}.npy".format(mask_no = i+1)
          
          mask_file = consolidated_masks[i,:,:,:]
          
          absolute_file_path = os.path.join(folder_path, file_name)
          
          np.save(absolute_file_path, mask_file)
          
          print("Mask {number} Saved!".format(number = i+1))
   
   
   
# segregate_masks(ROOT_DIR, masks_path)

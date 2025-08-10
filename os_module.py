#!/usr/bin/env python3
import os

def find_dir(path, target_dir):
  # print('working directory:', path)
  c_dirs = os.listdir(path)
  # print('c_dirs:', c_dirs)
  
  for d in c_dirs:
    if d.startswith('.'):
      continue
    
    new_path = f'{path}/{d}'
    # print('new_path:', new_path)
    
    if d == target_dir:
      print(new_path)

    find_dir(new_path, target_dir)

find_dir('./tree','python')

import shutil
import random
import os
directory = os.getcwd()
dirpath = os.path.join(directory, 'Sample_data')
destDirectory = os.path.join(directory, 'split_2')

filenames = random.sample(os.listdir(dirpath), 2)
for fname in filenames:
    srcpath = os.path.join(dirpath, fname)
    destPath = os.path.join(destDirectory, fname)
    shutil.copyfile(srcpath, destPath)

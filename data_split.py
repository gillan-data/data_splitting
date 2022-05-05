import shutil
import random
import os
directory = os.getcwd()
dirpath = os.path.join(directory, 'Sample_data')

j = [240, 960, 1920, 3840, 7680, 8640]

for i in j:
    destDirectory = os.path.join(directory, 'split_'+str(i))
    filenames = random.sample(os.listdir(dirpath), i)
    for fname in filenames:
        srcpath = os.path.join(dirpath, fname)
        destPath = os.path.join(destDirectory, fname)
        shutil.copyfile(srcpath, destPath)

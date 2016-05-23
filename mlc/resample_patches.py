import glob
classdirs = glob.glob('/Users/beijbom/gits/beijbom_web/mlc/patches_org/*')
import os
import numpy as np
import shutil
for cd in classdirs:
    nd = cd.replace('patches_org', 'patches')
    #os.makedirs(nd)
    files = glob.glob(cd + '/*.jpg')
    files = np.random.permutation(files)
    print files[1]
    for f in files[:500]:
        shutil.copyfile(f, f.replace('patches_org', 'patches'))
        
import os
import rasterio
import numpy as np

def load_patch(patch_dir):
    bands = []
    for file in sorted(os.listdir(patch_dir)):
        if file.endswith('.tif'):
            with rasterio.open(os.path.join(patch_dir, file)) as src:
                bands.append(src.read(1))
    return np.stack(bands, axis=0)

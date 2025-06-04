import os
import numpy as np
import matplotlib.pyplot as plt
import rasterio
from scripts.config import DATA_DIR

def show_sample_patch(patch_dir):
    bands=[]
    for file in sorted(os.listdir(patch_dir)):
        if file.endswith('.tif'):
            with rasterio.open(os.path.join(patch_dir,file)) as src:
                bands.append(src.read(1))

    fig, axs = plt.subplots(1,len(bands),figsize=(10,5))
    for i,band in enumerate(bands):
        axs[i].imshow(band,cmap='gray')
        axs[i].set_title(f"Band {i+1}")
    plt.tight_layout()
    plt.show()            
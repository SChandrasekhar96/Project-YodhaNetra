from scripts.visualize import show_sample_patch
from scripts.config import DATA_DIR
import os
if __name__=="__main__":
    sample_patch = os.path.join(DATA_DIR,'S1A')
    if os.path.exists(sample_patch):
        show_sample_patch(sample_patch)
    else:
        print(f"Sample patch not found at {sample_patch}. Please check the DATA_DIR path.")
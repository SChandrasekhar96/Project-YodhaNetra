import numpy as np
import matplotlib.pyplot as plt
def show_Dummy_Image():
    vv_band = np.random.rand(10,10)
    vh_band = np.random.rand(10,10)

    fig,axs = plt.subplots(1,2,figsize=(8,4))
    axs[0].imshow(vv_band, cmap='gray')
    axs[0].set_title('VV Band')

    axs[1].imshow(vh_band, cmap='gray')
    axs[1].set_title('VH Band')

    plt.tight_layout()
    plt.show()
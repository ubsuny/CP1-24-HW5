"""
here is how to graphe
"""
import pandas as pd
import os
import math as m
import numpy as np
import matplotlib.pyplot as plt


def plot_trans(data):
    """
    only one data input mabye, need to check
    needs to be a frequenc axis i think
    """

    forgraphfft = np.fft.fft(data).real
    forgraphifft = np.fft.ifft(forgraphfft).real

    freq = somthin

    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(freq, forgraphfft, label='FFT', color='red')
    plt.title('title')
    plt.xlabel('freq in some unit')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(freq, forgraphifft, label='IFFT', color='red')
    plt.title('title2')
    plt.xlabel('freq in some unit')
    plt.ylabel('Amplitude')
    plt.grid()

    plot = input("Do you want to save the plot? (yes/no): ").strip().lower()

    if plot == 'yes':
        fpath = input("enter where to save: ").strip()
        if not os.path.exists(fpath):
            print("Directory does not exist, try again")
        else:
            filpath = os.path.join(fpath, "put_name_of_imge.png")
            plt.savefig(filpath, format='png', dpi=600)
            print(f"Plot saved as {filpath}")
    else:
        print("Plot not saved.")

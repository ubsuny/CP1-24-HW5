"""
plots_ifft.py

to be deleated

"""
import pandas as pd
import os
import math as m
import numpy as np
import matplotlib.pyplot as plt


def plot_results(t, unalt_data, freq, magnitude, use_filt):
    plt.figure(figsize=(12, 8))

    if use_filt == 1:
        lble = 'IFFT using a threshhold'
    else:
        lble = 'IFFT'

    plt.subplot(2, 1, 1)
    plt.plot(t, unalt_data, label='Unalted data')
    plt.title('Original data')
    plt.xlabel('Time [s]')
    plt.ylabel('Your units of concern')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(freq, magnitude, label=lble)
    plt.title('Magnitude Spectrum')
    plt.xlabel('Frequency [Hz, 1/s]')
    plt.ylabel('Magnitude')
    plt.xlim(0, max(freq)/2)
    plt.legend()

    plt.tight_layout()

    plot = input("Do you want to save the plot? (yes/no): ").strip().lower()

    if plot == 'yes':
        fpath = input("enter where to save: ").strip()
        if not os.path.exists(fpath):
            print("Directory does not exist, try again")
        else:
            filpath = os.path.join(fpath, "workin on it.png")
            plt.savefig(filpath, format='png', dpi=600)
            print(f"Plot saved as {filpath}")
    else:
        print("Plot not saved.")

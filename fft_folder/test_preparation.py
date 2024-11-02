"""
test_preparation.py

this will be edited latter this is just for me atm

"""
import pandas as pd
import os
import math as m
import numpy as np
import matplotlib.pyplot as plt

from fft_folder.preparation import analyze_signal, anze_revm_trnd
from plots_ifft import plot_results


maxtime = 2
t = np.linspace(0, maxtime, 2000, endpoint=False)
f1, f2 = 50, 120
original_signal = np.sin(2*np.pi * f1 * t) + 0.5 * np.sin(2*np.pi * f2 * t)


freq, magnitude, main_frequencies, use_filt = analyze_signal(original_signal, maxtime, 'yes', 0.1)

plot_results(t, original_signal, freq, magnitude, use_filt)

print("Main Frequencies:", main_frequencies)

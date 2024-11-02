"""
test_inv_fft.py

"""
import pandas as pd
import os
import math as m
import numpy as np
import matplotlib.pyplot as plt

from inv_fft import analyze_signal, anze_revm_trnd
from plots_ifft import plot_results

fs = 1000
t = np.linspace(0, 5, fs, endpoint=False)
f1, f2 = 50, 120
original_signal = np.sin(np.pi * f1 * t) + 0.5 * np.sin(np.pi * f2 * t)


bins, magnitude, main_frequencies, use_filt = analyze_signal(original_signal, fs, 'yes', 0.1)

plot_results(t, original_signal, bins, magnitude, use_filt)

print("Main Frequencies:", main_frequencies)

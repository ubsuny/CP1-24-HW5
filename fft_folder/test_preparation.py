"""
test_preparation.py

this will be edited latter this is just for me atm

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from preparation import fft, calc_freq, inv_fft
from plots_ifft import plot_rets, anze_revm_trnd


#maxtime = 2
#t = np.linspace(0, maxtime, 2000, endpoint=False)
#f1, f2 = 50, 120
#original_signal = np.sin(2*np.pi * f1 * t) + 0.5 * np.sin(2*np.pi * f2 * t)


#freq, magnitude, main_frequencies, use_filt = analyze_signal(original_signal, maxtime, 'yes', 0.1)

# plot_results(t, original_signal, freq, magnitude, use_filt)

# print("Main Frequencies:", main_frequencies)

t = np.linspace(0, 2, 2000, endpoint=False)

f1, f2 = 50, 120

data = pd.Series(np.sin(f1*t)+0.5*np.sin(f2*t),index=range(0,len(t)))
# index_values = data.index.tolist()


freq = calc_freq(data)

plot_rets(freq,fft(data))
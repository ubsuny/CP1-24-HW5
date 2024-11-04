"""
preparation.py

fft
inverse fft
calculate frequencies
"""
import numpy as np

def fft(data):
    matrx = np.fft.fft(data)
    return np.abs(matrx)

def inv_fft(data):

    matrx = np.fft.fft(data)

    return np.fft.ifft(matrx)

def calc_freq(data):
    n = len(data)
    tim = data[n-1]
    freq = np.fft.fftfreq(n, tim/n)
    return freq

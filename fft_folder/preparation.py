"""
preparation.py

fft
inverse fft
calculate frequencies
"""
import numpy as np

def fft_powerspectrum(data):
    """This function interprates the csv data for you and calc the fft"""
    matrx = np.fft.fft(data)
    return np.abs(matrx)[:len(matrx/2)]

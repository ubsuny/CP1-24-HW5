"""
preparation.py

fft
inverse fft
calculate frequencies
"""
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def fft_powerspectrum(data):
    """This function takes the function in and outputs
    the powerspectrum"""
    matrx = np.fft.fft(data.values)
    return np.abs(matrx)[:len(matrx/2)]

def fft_mag(data):
    """this function is simalare to fft_powerspectrum only it does not cut the
    matrix in half or take the absolut values of the variables"""
    return np.fft.fft(data.values)


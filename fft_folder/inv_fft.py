"""
inv_fft.py
inverse fast fourie transform
"""
import pandas as pd
import os
import math as m
import numpy as np
import matplotlib.pyplot as plt

def get_main_freq(data):
    """
    take data from fft im pritty sure will check saturday
    """
    datafft = np.fft.fft(data).real
    
    
    return freqs
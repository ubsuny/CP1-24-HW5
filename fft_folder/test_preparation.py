"""
test_preparation.py

unit test for the functions fft_powerspectrum, fft_mag, inv_fft, calc_freq

"""
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
from preparation import fft_powerspectrum, fft_mag, inv_fft, calc_freq

trange = pd.date_range(datetime.now(), datetime.now()+timedelta(days=9),freq='d')
data = pd.Series([1,2,3,2,1,2,3,2,1,2],index=trange)

def test_fft_powerspectrum(time_series_data):
    """test the powerspectrums length and type of export"""
    powrspec = fft_powerspectrum(time_series_data)
    assert len(powrspec) == len(time_series_data)/2
    assert isinstance(powrspec, np.ndarray)

def test_fft_mag(time_series_data):
    """test the fft_mag length and type of export"""
    magnitudes = fft_mag(time_series_data)
    assert len(magnitudes) == len(time_series_data)
    assert isinstance(magnitudes, np.ndarray)

def test_inv_fft(time_series_data):
    """tests inv_fft length export aswell as testing to see if
    the fit matches the data"""
    invdata = inv_fft(fft_mag(time_series_data))
    assert len(invdata) == len(time_series_data)
    assert np.allclose(invdata, time_series_data.values, atol=1e-4)

def test_calc_freq(time_series_data):
    """calcs the length of the export of calc_freq"""
    freq = calc_freq(time_series_data, 'seconds')
    assert len(freq) == len(time_series_data)

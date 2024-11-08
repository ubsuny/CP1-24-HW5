"""
test_preparation.py
unit test for the functions fft_powerspectrum, fft_mag, inv_fft, calc_freq

"""
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
from preparation import fft_powerspectrum, fft_mag, inv_fft, calc_freq
import pytest

@pytest.fixture
def data():
    trange = pd.date_range(datetime.now(), datetime.now() + timedelta(days=9), freq='d')
    return pd.Series([1, 2, 3, 2, 1, 2, 3, 2, 1, 2], index=trange)

def test_fft_powerspectrum(data):
    """test the powerspectrums length and type of export"""
    powrspec = fft_powerspectrum(data)
    assert len(powrspec) == len(data)/2
    assert isinstance(powrspec, np.ndarray)

def test_fft_mag(data):
    """test the fft_mag length and type of export"""
    magnitudes = fft_mag(data)
    assert len(magnitudes) == len(data)
    assert isinstance(magnitudes, np.ndarray)

def test_inv_fft(data):
    """tests inv_fft length export aswell as testing to see if
    the fit matches the data"""
    invdata = inv_fft(fft_mag(data))
    assert len(invdata) == len(data)
    assert np.allclose(invdata, data.values, atol=1e-4)

def test_calc_freq(data):
    """calcs the length of the export of calc_freq"""
    freq = calc_freq(data, 'seconds')
    assert len(freq) == len(data)

"""

This module does unit test for padding and unpadding the data
"""
import pandas as pd
import matplotlib.pyplot as plt
from preparation import pad_time_series
from preparation import unpad_time_series

# Function to read the JSON file and return a time series with CO2/ concentration

data = pd.read_json('flask_monthly.json')

plt.scatter(data['Month'], data['CO2 (ppm)'])

x_ = data[data['Year'] == 1969]

# Example Usage
if __name__ == "__main__":
    # Sample time series
    # Create a datetime index using the Year and Month
    dates = pd.to_datetime(x_['Year'].astype(str) + '-' + x_['Month'].astype(str), format='%Y-%m')
    ts = pd.Series(x_['CO2 (ppm)'].values, index=dates) 
    # Use values for the data to avoid alignment issues

    print("Original Time Series:")
    print(ts)

    # Pad the series to length 12
    padded_ts = pad_time_series(ts, target_length=12)
    print("\nPadded Time Series:")
    print(padded_ts)

    # Unpad to get back the original series
    unpadded_ts = unpad_time_series(padded_ts, original_length=len(ts))
    print("\nUnpadded Time Series:")
    print(unpadded_ts)
=======
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

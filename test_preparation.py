"""
test_preparation.py
unit test for the functions fft_powerspectrum, fft_mag, inv_fft, calc_freq

"""
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
from preparation import fft_powerspectrum, fft_mag, inv_fft, calc_freq, remove_noise
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
    
def test_remove_low_frequency(synthetic_data):
    """Test remove_noise by removing low frequencies."""
    filtered_data = remove_noise(synthetic_data, low_freq=0.02, high_freq=None)
    assert filtered_data is not None, "Filtered data is None"
    assert (np.abs(np.fft.fft(filtered_data.values)[:10]) < 0.1).all(), "Low-frequency components were not removed correctly"

def test_remove_high_frequency(synthetic_data):
    """Test remove_noise by removing high frequencies."""
    filtered_data = remove_noise(synthetic_data, low_freq=None, high_freq=0.02)
    assert filtered_data is not None, "Filtered data is None"
    assert (np.abs(np.fft.fft(filtered_data.values)[20:]) < 0.1).all(), "High-frequency components were not removed correctly"

def test_full_bandpass_filter(synthetic_data):
    """Test remove_noise with a bandpass filter for specific frequency range."""
    filtered_data = remove_noise(synthetic_data, low_freq=0.01, high_freq=0.05)
    assert filtered_data is not None, "Filtered data is None"
    fft_values = np.abs(np.fft.fft(filtered_data.values))
    freqs = np.fft.fftfreq(len(filtered_data), d=(filtered_data.index[1] - filtered_data.index[0]).total_seconds())
    assert (fft_values[np.abs(freqs) < 0.01] < 0.1).all(), "Low frequencies not removed correctly"
    assert (fft_values[np.abs(freqs) > 0.05] < 0.1).all(), "High frequencies not removed correctly"

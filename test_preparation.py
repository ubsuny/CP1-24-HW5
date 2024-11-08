"""
test_preparation.py
unit test for the functions fft_powerspectrum, fft_mag, inv_fft, calc_freq

"""
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
from preparation import fft_powerspectrum, fft_mag, inv_fft, calc_freq, find_peak_frequencies
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

# Testing the determination of the frequency of the peak(s)
def test_single_frequency():
    """ Tests for the presence of a single frequency """
    fs = 1000  # Sampling frequency in Hz
    period = 1.0 / fs  # Sampling period
    signal_length = 1000  # Length of signal
    t = np.linspace(0.0, signal_length * period, signal_length, endpoint = False)

    # Generate a signal with a known single frequency at 50 Hz
    frequency = 50
    signal = np.sin(2 * np.pi * frequency * t)

    # Convert signal to a pd.Series with a DatetimeIndex
    time_index = pd.date_range(start="2023-01-01", periods=signal_length,
                               freq=pd.Timedelta(seconds=period))
    signal_series = pd.Series(signal, index=time_index)

    # Find peak frequencies
    peak_frequencies = find_peak_frequencies(signal_series)

    # Check if the detected frequency is close to 50 Hz
    failed = "Failed to detect the correct frequency."
    assert any(np.isclose(peak_frequencies, frequency, atol=1)), failed

def test_multiple_frequencies():
    """ Tests for the presence of multiple frequencies """
    fs = 1000  # Sampling frequency in Hz
    period = 1.0 / fs  # Sampling period
    signal_length = 1000  # Length of signal
    t = np.linspace(0.0, signal_length * period, signal_length, endpoint=False)

    # Generate a signal with multiple known frequencies
    frequencies = [50, 120]
    signal = np.sin(2 * np.pi * frequencies[0] * t) + np.sin(2 * np.pi * frequencies[1] * t)

    # Convert signal to a pd.Series with a DatetimeIndex
    time_index = pd.date_range(start="2023-01-01", periods=signal_length,
                               freq=pd.Timedelta(seconds=period))
    signal_series = pd.Series(signal, index=time_index)

    # Find peak frequencies
    peak_frequencies = find_peak_frequencies(signal_series)

    # Check if the detected frequencies include 50 Hz and 120 Hz
    for freq in frequencies:
        failed = f"Failed to detect frequency {freq} Hz."
        assert any(np.isclose(peak_frequencies, freq, atol=1)), failed

def test_no_signal():
    """ Tests for the case of no present frequencey to get detected """
    fs = 1000  # Sampling frequency in Hz
    period = 1.0 / fs  # Sampling period
    signal_length = 1000  # Length of signal
    signal = np.zeros(1000)  # A zero signal

    # Convert signal to a pd.Series with a DatetimeIndex
    time_index = pd.date_range(start="2023-01-01", periods=signal_length,
                               freq=pd.Timedelta(seconds=period))
    signal_series = pd.Series(signal, index=time_index)

    # Find peak frequencies
    peak_frequencies = find_peak_frequencies(signal_series)

    # Check if no peaks are found
    assert len(peak_frequencies) == 0, "Detected frequencies in a zero signal."

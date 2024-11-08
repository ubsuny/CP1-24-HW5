"""
test_preparation.py
unit test for the functions fft_powerspectrum, fft_mag, inv_fft, calc_freq

"""
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
from preparation import fft_powerspectrum, fft_mag, inv_fft, calc_freq,window,unwindow
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


def test_window():
    """
    test_window tests whether or not the start
    and end point of the windowed data are zero
    for each window function.
    """
    #Test data is made from a sin wave
    x=np.linspace(0,2*np.pi,100)
    start=24
    end=75
    func=[np.sin(i) for i in x]
    data=pd.Series(func,index=x)
    #the test data is windowed and the 
    #endpoints are checked.
    windows=window(data, start,end)
    ydata=windows["Hann Window"].values
    assert ydata[0]==0
    assert ydata[len(ydata)-1]==0
    ydata=windows["Blackman Window"].values
    assert ydata[0]==0
    assert ydata[len(ydata)-1]==0
    ydata=windows["Welch Window"].values
    assert ydata[0]==0
    assert ydata[len(ydata)-1]==0
def test_unwindow():
    """
    test_unwindow ensures that the unwindow function
    reverses the window function. Does this for
    each window function.
    """
    x=np.linspace(0,2*np.pi,100)
    start=24
    end=75
    func=[np.sin(i) for i in x]
    data=pd.Series(func,index=x)
    windows=window(data, start,end)
    new=unwindow(windows["Hann Window"],"Hann Window")
    count=0
    test_func=func[start+1:end]
    for i in test_func:
        #Rounding to the third decimal place is necessary
        #to get this to work.
        assert round(i,3)==round(new.values[count],3)
        count+=1
    
    new=unwindow(windows["Blackman Window"],"Blackman Window")
    count=0
    for i in test_func:
        assert round(i,3)==round(new.values[count],3)
        count+=1
    
    new=unwindow(windows["Welch Window"],"Welch Window")
    count=0
    for i in test_func:
        assert round(i,3)==round(new.values[count],3)
        count+=1

def test_calc_freq(data):
    """calcs the length of the export of calc_freq"""
    freq = calc_freq(data, 'seconds')
    assert len(freq) == len(data)


"""
test_preparation.py

unit test for the functions fft, calc_freq, inv_fft

"""

from datetime import datetime, timedelta
import numpy as np
import pandas as pd

from preparation import fft_powerspectrum, fft_mag, get_timeseries

#from thid import plot_rets

"""
t = np.linspace(0, 2, 2000, endpoint=False)
f1, f2 = 50, 120
data = pd.Series(np.sin(f1*t)+0.5*np.sin(f2*t),index=range(0,len(t)))
# index_values = data.index.tolist()
freq = calc_freq(data)
print(freq)
print(inv_fft(data))
print(data)
plot_rets(freq,fft(data))
"""

t = np.linspace(0, 2, 2000, endpoint=False)
f1, f2 = 50, 120
data = pd.Series(np.sin(2*np.pi*f1*t)+0.5*np.sin(2*np.pi*f2*t),index=range(0,len(t)))

#trange = date_range(datetime.now(), datetime.now()+pd.timedelta(days=9),freq='d')
#trange[i].timestamp()

"""
def test_fft(data):

    magnitudes = fft(data)
    assert len(magnitudes) == len(data)

def test_calc_freq(data, f1, f2):            
    freq = calc_freq(data)
    lngth = len(data)/2
    newf1 = f1 + lngth
    newf2 = f2 + lngth
    assert len(freq) == len(data)
    assert freq[newf1] > 200
    assert freq[newf2] > 200

def test_inv_fft(data):
    invdata = inv_fft(data)
    assert len(invdata) == len(data)
"""

def test_get_timeseries_date_column_length():
    '''
    This function tests that the length of co2_series (output of get_timeseries) 
    has the same length of the original file.
    '''
    co2_series = get_timeseries('/mauna-loa-data/flask_monthly.json')

    #Check that the length of the Series matches the original data length
    original_data = pd.read_json('/mauna-loa-data/flask_monthly.json')
    original_length = len(original_data)  # Count of rows in the JSON data
    assert len(co2_series) == original_length, (
        "Length of the datetime index should match the length of the original Month column."
    )

matr = fft_powerspectrum(data)

print(matr)

#freq = calc_freq(data)
# plot_rets(freq,fft(data))

#print(np.isclose(0, 0.0001, atol=0.001))

trange = pd.date_range(datetime.now(), datetime.now()+timedelta(days=9),freq='d')
data1 = pd.Series([1,2,3,4,5,6,7,8,9,10],index=trange)



print(len(data1))

print(data1.index[0].timestamp())


print(data1.iloc[2] * 1)


"""
This module does padding and unpadding the data
"""
import pandas as pd

def pad_time_series(series, target_length, padding_value=None):
    """
    Pads the given time series to the target length.

    Parameters:
    - series: pd.series
        The input time series with datetime index.
    - target_length: int
        The desired length after padding.
    - padding_value: float or None
        The value to pad with. If None, will use the mean of the series.
    Returns:
    - pd.series
        The padded time series.
    """
    # Determine current length
    current_length = len(series)

    # If current length is already equal to or greater than target, return the series
    if current_length >= target_length:
        return series

    # Determine padding length
    padding_length = target_length - current_length

    # If no padding value is provided, calculate a reasonable padding value
    if padding_value is None:
        padding_value = series.mean()  # You could also use median or any other method

    # Create a padding Series
    padding_index = pd.date_range(start=series.index[-1] + pd.Timedelta(days=1), 
                               periods=padding_length, freq='D')
    padding_series = pd.Series(padding_value, index=padding_index)

    # Concatenate the original series with the padding
    padded_series = pd.concat([series, padding_series])

    return padded_series


def unpad_time_series(padded_series, original_length):
    """
    Unpads the given time series to the original length.

    Parameters:
    - padded_series: pd.Series
        The padded time series with datetime index.
    - original_length: int
        The original length of the series before padding.

    Returns:
    - pd.Series
        The unpadded time series.
    """
    # Return the original length of the series
    return padded_series.iloc[:original_length]

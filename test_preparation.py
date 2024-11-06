"""
test_preparation.py

unit test for the functions fft, calc_freq, inv_fft
unit test for padding and unpadding the data
"""

from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from preparation import pad_time_series
from preparation import unpad_time_series
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

"""
preparation.py

this code creates the functions needed to run the
fft, invs ffft and to calculate the frequencies
fft
inverse fft
calculate frequencies
"""

import numpy as np
import pandas as pd


def fft_powerspectrum(data):
    """This function takes the function in and outputs
    the powerspectrum"""
    n = len(data)
    timestamp_sum = sum(data.index[i+1].timestamp() - data.index[i].timestamp() for i in range(n-1))
    if not timestamp_sum/(n-1) == data.index[2].timestamp() - data.index[1].timestamp():
        print("Data is not evenly spaced or data points are missing")
        return None
    matrx = np.fft.fft(data.values)
    return np.abs(matrx)[:n // 2]


def fft_mag(data):
    """this function is simalare to fft_powerspectrum only it does not cut the
    matrix in half or take the absolut values of the variables"""
    n = len(data)
    timestamp_sum = sum(data.index[i+1].timestamp() - data.index[i].timestamp() for i in range(n-1))
    compare = np.isclose(timestamp_sum/(n-1),
                          data.index[2].timestamp() - data.index[1].timestamp(), atol=1e-6)
    if not compare:
        print("Data is not evenly spaced or data points are missing")
        return None
    return np.fft.fft(data.values)

def inv_fft(mag):
    """this invers fft's input is the output of the fft_mag function
    do not enter in the fft_powerspectrum cause the output of this would be wrong
    ie not inv_fft(fft_powerspectrum(data)), but inv_fft(fft_mag(data))"""
    newthing = np.fft.ifft(mag)
    return np.abs(newthing)

def calc_freq(data, tim):
    """this takes in the same data as the fft equations only gives the frequencies
    of the data, this gives out the frequencies in Hz, if you want to change it to
    days say day in the second imput, or if you want it in months say month (ie 365.25/12 days) """
    n = len(data)
    timestamp_sum = sum(data.index[i+1].timestamp() - data.index[i].timestamp() for i in range(n-1))
    diftim = data.index[2].timestamp() - data.index[1].timestamp()
    if not timestamp_sum/(n-1) == diftim:
        print("Data is not evenly spaced or data points are missing")
        return None
    if tim.strip().lower() == 'day':
        diftim = diftim/(60*60*24)
    if tim.strip().lower() == 'month':
        diftim = diftim/(60*60*24*30.4375)
    return np.fft.fftfreq(n, d = diftim)

def get_timeseries(path, datecolumn = 'date', datacolumn = 'CO2 (ppm)'):
    '''
    This function reads json files from the data collection task 
    and returns a pandas time series with datetime as index and 
    concentration of CO2/Methane as data.

    Once the path is specified, we can plot the time series using a simple matplotlib code
    plt.figure(figsize=(10, 6))
    co2_series.plot()
    plt.title("CO2 Concentration Over Time")
    plt.xlabel("Date")
    plt.ylabel("CO2 (ppm)")
    plt.grid(True)
    plt.show()

    Parameters:
    - path: Stringlike. path/to/json/file.json
    - datecolumn: to specifiy specific date column name

    Returns:
    - Pandas Time Series. Index = Datetime, Data = CO2/Methane Concentration
    '''

    #Extracts data from the json file at the input path
    data = pd.read_json(path)
    #Uses the month and year information from the json file,
    # assumes data was taken on the first of each month,
    # creates new column with datetime
    
    if datecolumn == "date": 
        data['date'] = pd.to_datetime(data[['Year', 'Month']].assign(Day=1))

    #Sets datetime as index
    data.set_index(datecolumn, inplace=True)

    #Creates timeseries with co2 (ppm) as data and datetime as index
    co2_series = data[datacolumn]


    return co2_series

def remove_noise(data, low_freq=None, high_freq=None):
    """
    Removes high/low frequency noise from a time-series by applying a bandpass filter in the frequency domain.

    Parameters:
    data (pd.Series): Time series data with a datetime index.
    low_freq (float): The minimum frequency to retain; frequencies below this are considered noise and removed.
    high_freq (float): The maximum frequency to retain; frequencies above this are considered noise and removed.
    
    Returns:
    pd.Series: Filtered time series with noise removed, same length as the input.
    """
    # Ensure data is evenly spaced
    n = len(data)
    timestamp_sum = sum(data.index[i+1].timestamp() - data.index[i].timestamp() for i in range(n-1))
    if not timestamp_sum / (n-1) == data.index[2].timestamp() - data.index[1].timestamp():
        print("Data is not evenly spaced or data points are missing")
        return None

# FFT to get the frequency components
    data_fft = np.fft.fft(data.values)
    freqs = np.fft.fftfreq(n, d=(data.index[1] - data.index[0]).total_seconds())
    
    # Apply the frequency filter
    if low_freq is not None:
        data_fft[np.abs(freqs) < low_freq] = 0
    if high_freq is not None:
        data_fft[np.abs(freqs) > high_freq] = 0

    # Inverse FFT to get the filtered time-domain signal
    filtered_data = np.fft.ifft(data_fft)
    
    # Return as a pandas series with the original datetime index
    return pd.Series(filtered_data.real, index=data.index)

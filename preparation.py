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
    """Outputs the power spectrum of the input time series data."""
    n = len(data)
    if n < 2:
        print("Insufficient data points for FFT.")
        return None
    
    timestamp_diff = np.diff(data.index.to_series().astype(np.int64) // 10**9)  # convert to seconds
    mean_interval = timestamp_diff.mean()
    
    if not np.allclose(timestamp_diff, mean_interval, rtol=1e-5):
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
    """Calculates frequency bins for FFT with units specified by `tim` parameter."""
    n = len(data)
    if n < 2:
        print("Insufficient data points for frequency calculation.")
        return None

    timestamp_diff = np.diff(data.index.to_series().astype(np.int64) // 10**9)  # convert to seconds
    mean_interval = timestamp_diff.mean()

    if not np.allclose(timestamp_diff, mean_interval, rtol=1e-5):
        print("Data is not evenly spaced or data points are missing")
        return None
    # Adjust sampling interval based on specified units
    if tim.strip().lower() == 'day':
        mean_interval /= (60 * 60 * 24)
    elif tim.strip().lower() == 'month':
        mean_interval /= (60 * 60 * 24 * 30.4375)

    return np.fft.fftfreq(n, d=mean_interval)

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

"""
preparation.py

fft
inverse fft
calculate frequencies
"""

import numpy as np
import pandas as pd


def fft_powerspectrum(data):
    """This function takes the function in and outputs
    the powerspectrum"""
    matrx = np.fft.fft(data.values)
    return np.abs(matrx)[:len(matrx/2)]

def fft_mag(data):
    """this function is simalare to fft_powerspectrum only it does not cut the
    matrix in half or take the absolut values of the variables"""
    return np.fft.fft(data.values)

def get_timeseries(path):
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

    Returns:
    - Pandas Time Series. Index = Datetime, Data = CO2/Methane Concentration
    '''

    #Extracts data from the json file at the input path
    data = pd.read_json(path)
    #Uses the month and year information from the json file,
    # assumes data was taken on the first of each month,
    # creates new column with datetime
    data['date'] = pd.to_datetime(data[['Year', 'Month']].assign(Day=1))

    #Sets datetime as index
    data.set_index('date', inplace=True)

    #Creates timeseries with co2 (ppm) as data and datetime as index
    co2_series = data['CO2 (ppm)']


    return co2_series

"""
This module does padding and unpadding the data
"""

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

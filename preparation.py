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

    # Convert JSON to a DataFrame
    df = pd.DataFrame(data)

    #Uses the month and year information from the json file,
    # assumes data was taken on the first of each month,
    # creates new column with datetime
    df['Date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))

    #Creates timeseries with co2 (ppm) as data and datetime as index
    co2_series = df.set_index('Date')['CO2 (ppm)']

    return co2_series

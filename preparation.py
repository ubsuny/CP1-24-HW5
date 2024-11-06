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

#These constants are used for the blackman_window function
A0=.42
A1=.5
A2=.08

hann_window=lambda N, n: np.sin(np.pi*n/N)**2
"""
This acts as the hann window function
"""
blackman_window=lambda N, n:A0-A1*np.cos(np.pi*2*n/N)+A2*np.cos(4*np.pi*n/N)
"""
This acts as the blackman_window function
"""
welch_window= lambda N, n: 1-((n-N/2)/(N/2))**2
"""
This acts as the welch window function
"""

def window(data, start, end):
    """
    the window function takes in a pandas timeseries,
    a start index, and an end index defining the range
    of the window. It returns a dictionary with key values
    being the name of the window function applied and 
    then a new timeseries for each window function
    """
    tdata=data.index
    ydata=data.values
    N=end-start+1
    windowed=[]
    time_windowed=[]

    #Loops are applied to go through the range and apply
    #the window function to each index of the data within
    #the range
    for i in range(start,end+1):
        windowed.append(hann_window(N,i)*ydata[i])
        time_windowed.append(tdata[i])

    hann=pd.Series(windowed,index=time_windowed)
    windowed=[]

    for i in range(start,end+1):
        windowed.append(blackman_window(N,i)*ydata[i])

    black=pd.Series(windowed, index=time_windowed)

    windowed=[]
    for i in range(start,end+1):
        windowed.append(welch_window(N,i)*ydata[i])
    
    welch=pd.Series(windowed,index=time_windowed)

    return {"Hann Window": hann, "Blackman Window":black, "Welch Window":welch}

def unwindow(data, type):
    """
    unwindow takes in a pandas time series and a string
    defining the type of window function to undo. It then
    undos that window function.
    """
    ydata=data.values
    tdata=data.time
    unwindowed=[]
    time_unwindowed=[]
    N=len(ydata)
    
    #Because the window function makes the start and 
    #end points of the original data zero, that info
    #is lost. With this, the start and end points are
    #excluded from the unwindow process.
    if type=="Hann Window":
        for i in range(1,len(ydata)-1):
            unwindowed.append(ydata[i]*1/hann_window(N,i))
            time_unwindowed.append(tdata[i])
    if type=="Blackman Window":
        for i in range(1, len(ydata)-1):
            unwindowed.append(ydata[i]*1/blackman_window(N,i))
            time_unwindowed.append(tdata[i])
    if type=="Welch Window":
        for i in range(1, len(ydata)-1):
            unwindowed.append(ydata[i]*1/welch_window(N,i))
            time_unwindowed.append(tdata[i])
            
    return pd.Series(unwindowed, index=time_unwindowed)

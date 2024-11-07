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
    if not timestamp_sum/(n-1) == data.index[2].timestamp() - data.index[1].timestamp():
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


A0=.42
A1=.5
A2=.08

def hann_window(big_n,n):
    """
    This acts as the hann window function
    """
    return np.sin(np.pi*n/big_n)**2

def blackman_window(big_n,n):
    """
    This acts as the blackman_window function
    """
    return A0-A1*np.cos(np.pi*2*n/big_n)+A2*np.cos(4*np.pi*n/big_n)

def welch_window(big_n,n):
    """
    This acts as the welch window function
    """
    return 1-((n-big_n/2)/(big_n/2))**2


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
    big_n=end-start
    windowed=[]
    time_windowed=[]

    #Loops are applied to go through the range and apply
    #the window function to each index of the data within
    #the range
    for i in range(start,end+1):
        windowed.append(round(hann_window(big_n,i-start)*ydata[i],9))
        time_windowed.append(tdata[i])
    hann=pd.Series(windowed,index=time_windowed)
    windowed=[]

    for i in range(start,end+1):
        windowed.append(round(blackman_window(big_n,i-start)*ydata[i],9))

    black=pd.Series(windowed, index=time_windowed)

    windowed=[]
    for i in range(start,end+1):
        windowed.append(welch_window(big_n,i-start)*ydata[i])
    
    welch=pd.Series(windowed,index=time_windowed)

    return {"Hann Window": hann, "Blackman Window":black, "Welch Window":welch}

def unwindow(data, type):
    """
    unwindow takes in a pandas time series and a string
    defining the type of window function to undo. It then
    undos that window function.
    """
    ydata=data.values
    tdata=data.index
    unwindowed=[]
    time_unwindowed=[]
    big_n=len(ydata)-1
    
    #Because the window function makes the start and 
    #end points of the original data zero, that info
    #is lost. With this, the start and end points are
    #excluded from the unwindow process.
    if type=="Hann Window":
        for i in range(1,len(ydata)-1):
            unwindowed.append(ydata[i]*1/hann_window(big_n,i))
            print(ydata[i]/hann_window(big_n,i))
            time_unwindowed.append(tdata[i])
    if type=="Blackman Window":
        for i in range(1, len(ydata)-1):
            unwindowed.append(ydata[i]*1/blackman_window(big_n,i))
            time_unwindowed.append(tdata[i])
    if type=="Welch Window":
        for i in range(1, len(ydata)-1):
            unwindowed.append(ydata[i]*1/welch_window(big_n,i))
            time_unwindowed.append(tdata[i])

    return pd.Series(unwindowed, index=time_unwindowed)


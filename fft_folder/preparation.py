"""
preparation.py

"""
import numpy as np

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
import numpy as np
import pandas as pd

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

# Example usage
# Remove high and low frequency noise
filtered_data = remove_noise(data, low_freq=0.001, high_freq=0.05)

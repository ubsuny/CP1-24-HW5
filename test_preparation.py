"""

This module does unit test for padding and unpadding the data
"""
import pandas as pd
import matplotlib.pyplot as plt
from preparation import pad_time_series
from preparation import unpad_time_series

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

"""
This module does padding and unpadding the data
"""
import pandas as pd

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

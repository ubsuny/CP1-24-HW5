"""
Module to load, process, and save CO₂ concentration data from the Mauna Loa Observatory.

This module performs the following tasks:
1. Loads a CO₂ data file from the Mauna Loa Observatory's flask sampling dataset.
2. Extracts relevant columns: Timestamp, Fractional Year, CO₂ concentration (ppm), and standard deviation (ppm).
3. Saves the processed data as both a CSV and a JSON file.

Dependencies:
    - pandas: for loading, processing, and saving the data.

File Structure:
    - Input file: 'mauna-loa/flask-discrete/flask_discrete.txt' (raw data file)
    - Output files:
        - CSV: 'mauna-loa/flask-discrete/flask_discrete.csv'
        - JSON: 'mauna-loa/flask-discrete/flask_discrete.json'
"""

import pandas as pd

# Load the file, skipping the metadata rows
# Assign NaN to -999.99 nonsensical values
df = pd.read_csv('mauna-loa/flask-discrete/flask_discrete.txt', delim_whitespace=True, skiprows=149, na_values="-999.99")

# Extract relevant columns
df_extracted = df[['datetime', 'time_decimal', 'value', 'value_unc']]

# Assign more meaningful names to columns
df_extracted.columns = ['Timestamp', 'Fractional Year', 'CO2 (ppm)', 'Standard Deviation (ppm)']

# Output to CSV
df_extracted.to_csv('mauna-loa/flask-discrete/flask_discrete.csv', index=False)

# Convert to JSON and save it
df_extracted.to_json('mauna-loa/flask-discrete/flask_discrete.json', orient='records', date_format='iso')

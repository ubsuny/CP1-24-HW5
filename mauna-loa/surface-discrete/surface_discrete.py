"""
Module to load, process, and save CO₂ concentration data from the Mauna Loa Observatory.

This module performs the following tasks:
1. Loads a CO₂ data file from the Mauna Loa Observatory's Surface PFP sampling dataset.
2. Extracts relevant columns: Timestamp, Fractional Year, CO₂ concentration (ppm), and standard
deviation (ppm).
3. Saves the processed data as a CSV, JSON, and Markdown file, and an additional JSON file with
no NaN values.

Dependencies:
    - pandas: for loading, processing, and saving the data.

File Structure:
    - Input file: 'mauna-loa/surface-discrete/surface_discrete_raw.txt' (raw data file)
    - Output files:
        - CSV: 'mauna-loa/surface-discrete/surface_discrete.csv'
        - JSON: 'mauna-loa/surface-discrete/surface_discrete.json'
        - JSON without NaN: 'mauna-loa/surface-discrete/surface_discrete_no_nan.json'
        - Markdown: 'mauna-loa/surface-discrete/surface_discrete.md'
"""

import pandas as pd

# Load the file, skipping the metadata rows and treating nonsensical values as NaN
df = pd.read_csv('mauna-loa/surface-discrete/surface_discrete_raw.txt', delim_whitespace=True,
                 skiprows=147, na_values="-999.99")

# Extract relevant columns
df_extracted = df[['datetime', 'time_decimal', 'value', 'value_unc']]

# Assign more meaningful names to columns
df_extracted.columns = ['Timestamp', 'Fractional Year', 'CO2 (ppm)', 'Standard Deviation (ppm)']

# Convert 'Timestamp' to datetime format
df_extracted['Timestamp'] = pd.to_datetime(df_extracted['Timestamp'], utc=True)

# Output to CSV
df_extracted.to_csv('mauna-loa/surface-discrete/surface_discrete.csv', index=False)

# Convert to JSON and save it
df_extracted.to_json('mauna-loa/surface-discrete/surface_discrete.json', orient='records',
                     date_format='iso')

# Create a filtered JSON file without NaN values
df_extracted.dropna().to_json('mauna-loa/surface-discrete/surface_discrete_no_nan.json',
                              orient='records', date_format='iso')

# Convert to Markdown and save it
with open('mauna-loa/surface-discrete/surface_discrete.md', 'w', encoding='utf-8') as md_file:
    md_file.write(df_extracted.to_markdown(index=False))

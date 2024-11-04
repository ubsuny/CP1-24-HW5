"""
Module to load, process, and save CO₂ concentration data from the
Mauna Loa Observatory.

This module performs the following tasks:
1. Loads a CO₂ data file from the Mauna Loa Observatory's flask sampling
dataset.
2. Extracts relevant columns: year, month, and CO₂ concentration (ppm).
3. Saves the processed data as a CSV, JSON, and Markdown file, and an
additional JSON file
with no NaN values.
Dependencies:
    - pandas: for loading, processing, and saving the data.

File Structure:
    - Input file: 'mauna-loa/flask-monthly/flask_monthly_raw.txt'
    (raw data file)
    - Output files:
        - CSV: 'mauna-loa/flask-monthly/flask_monthly.csv'
        - JSON: 'mauna-loa/flask-monthly/flask_monthly.json'
        - JSON without NaN: 'mauna-loa/flask-monthly/flask_monthly_no_nan.json'
        - Markdown: 'mauna-loa/flask-monthly/flask_monthly.md'
"""

import pandas as pd

# Load the file, skipping the metadata rows
# Treating '-999.99' as NaN for missing values
df = pd.read_csv('mauna-loa/flask-monthly/flask_monthly_raw.txt', delim_whitespace=True,
                 skiprows=53, na_values="-999.99")

# Extract relevant columns
df_extracted = df[["year", "month", "value"]]

# Rename the 'value' column to 'CO2 (ppm)' in the extracted DataFrame
df_extracted.rename(columns={'value': 'CO2 (ppm)'}, inplace=True)

# Combine 'year' and 'month' into a single 'Timestamp' column and convert to datetime
df_extracted['Timestamp'] = pd.to_datetime(df_extracted[['year', 'month']].assign(DAY=1))

# Drop the original 'year' and 'month' columns
df_extracted.drop(columns=['year', 'month'], inplace=True)

# Reorder columns to have 'Timestamp' first
df_extracted = df_extracted[['Timestamp', 'CO2 (ppm)']]

# Output to CSV
df_extracted.to_csv('mauna-loa/flask-monthly/flask_monthly.csv', index=False)

# Convert to JSON and save it
df_extracted.to_json('mauna-loa/flask-monthly/flask_monthly.json', orient='records',
                     date_format='iso')

# Create a filtered JSON file without NaN values
df_extracted.dropna().to_json('mauna-loa/flask-monthly/flask_monthly_no_nan.json',
                              orient='records', date_format='iso')

# Convert to Markdown and save it
with open('mauna-loa/flask-monthly/flask_monthly.md', 'w', encoding='utf-8') as md_file:
    md_file.write(df_extracted.to_markdown(index=False))

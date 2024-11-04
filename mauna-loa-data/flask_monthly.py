"""
Module to load, process, and save CO₂ concentration data from the Mauna Loa Observatory.

This module performs the following tasks:
1. Loads a CO₂ data file from the Mauna Loa Observatory's flask sampling dataset.
2. Extracts relevant columns: Year, Month, and CO₂ concentration (ppm).
3. Saves the processed data as a CSV, JSON, and Markdown file, and an additional JSON file with no NaN values.
Dependencies:
    - pandas: for loading, processing, and saving the data.

File Structure:
    - Input file: 'mauna-loa-data/flask-monthly/flask_monthly_raw.txt' (raw data file)
    - Output files:
        - CSV: 'mauna-loa-data/flask-monthly/flask_monthly.csv'
        - JSON: 'mauna-loa-data/flask-monthly/flask_monthly.json'
        - JSON without NaN: 'mauna-loa-data/flask-monthly/flask_monthly_no_nan.json'
        - Markdown: 'mauna-loa-data/flask-monthly/flask_monthly.md'
"""

import pandas as pd

# Load the file, skipping the metadata rows and treating '-999.99' as NaN for missing values
df = pd.read_csv('mauna-loa-data/flask-monthly/flask_monthly_raw.txt', delim_whitespace=True, skiprows=54, na_values="-999.99")

# Extract relevant columns
df_extracted = df[["Year", "Month", "Value"]]

# Rename the 'Value' column to 'CO2 (ppm)' in the extracted DataFrame
df_extracted.rename(columns={'Value': 'CO2 (ppm)'}, inplace=True)

# Output to CSV
df_extracted.to_csv('mauna-loa-data/flask-monthly/flask_monthly.csv', index=False)

# Convert to JSON and save it
df_extracted.to_json('mauna-loa-data/flask-monthly/flask_monthly.json', orient='records', date_format='iso')

# Create a filtered JSON file without NaN values
df_extracted.dropna().to_json('mauna-loa-data/flask-monthly/flask_monthly_no_nan.json', orient='records', date_format='iso')

# Convert to Markdown and save it
with open('mauna-loa-data/flask-monthly/flask_monthly.md', 'w') as md_file:
    md_file.write(df_extracted.to_markdown(index=False))

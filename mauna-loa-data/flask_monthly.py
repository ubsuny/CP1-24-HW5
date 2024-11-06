"""
Module to load, process, and save CO₂ concentration data from the Mauna Loa Observatory.

This module performs the following tasks:
1. Loads a raw CO₂ data file from the Mauna Loa Observatory's flask sampling dataset, handling missing values and metadata.
2. Extracts the relevant columns: Year, Month, and CO₂ concentration (ppm).
3. Saves the processed data to multiple formats:
   - CSV file for general use.
   - JSON file in ISO format, with an additional JSON file excluding NaN values.
   - Markdown file for easier viewing and sharing of data tables.
4. Creates a time series plot of CO₂ concentration over time.

Dependencies:
    - pandas: for loading, processing, and saving the data.
    - matplotlib: for plotting the time series.

File Structure:
    - Input file:
        - 'mauna-loa-data/flask_monthly_raw.txt'
    - Output files:
        - CSV: 'mauna-loa-data/flask_monthly.csv'
        - JSON: 'mauna-loa-data/flask_monthly.json'
        - JSON without NaN: 'mauna-loa-data/flask_monthly_no_nan.json'
        - Markdown: 'mauna-loa-data/flask_monthly.md'
    - Plot:
        - A time series plot of CO₂ concentration over time, created with matplotlib.

Usage:
    - Call this module to load and process the data from 'flask_monthly_raw.txt'.
    - Processed data files will be saved in the specified output formats.
    - Run the plotting section to visualize CO₂ concentration as a function of time.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the file, skipping the metadata rows and treating '-999.99' as NaN for missing values
df = pd.read_csv('mauna-loa-data/flask_monthly_raw.txt', delim_whitespace=True, skiprows=53, na_values="-999.99")

# Extract relevant columns
df_extracted = df[["year", "month", "value"]]

# Rename the 'Value' column to 'CO2 (ppm)' in the extracted DataFrame
df_extracted.rename(columns={'value': 'CO2 (ppm)'}, inplace=True)

# Output to CSV
df_extracted.to_csv('mauna-loa-data/flask_monthly.csv', index=False)

# Convert to JSON and save it
df_extracted.to_json('mauna-loa-data/flask_monthly.json', orient='records', date_format='iso')

# Create a filtered JSON file without NaN values
df_extracted.dropna().to_json('mauna-loa-data/flask_monthly_no_nan.json', orient='records', date_format='iso')

# Convert to Markdown and save it
with open('mauna-loa-data/flask_monthly.md', 'w') as md_file:
    md_file.write(df_extracted.to_markdown(index=False))

# Extract data from JSON file
path = 'mauna-loa-data/flask_monthly.json'
data = pd.read_json(path)

# Create datetime data

data['date'] = pd.to_datetime(data[['year', 'month']].assign(Day=1))

data.set_index('date', inplace=True)

co2_series = data['CO2 (ppm)']

# Plot as timeseries

plt.figure(figsize=(10, 6))
co2_series.plot()
plt.title("CO2 Concentration Over Time")
plt.xlabel("Date")
plt.ylabel("CO2 (ppm)")
plt.grid(True)
plt.show()

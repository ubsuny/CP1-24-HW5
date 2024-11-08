"""
This module converts a number of CO2 data files as
.txt files into a single panda dataframe
with only the datetime and CO2 (ppm) values.
"""
import pandas as pd

# List of file paths
file_paths = ["Africa_Data.txt", "Asia_Data.txt", "NA_Data.txt", "SA_Data.txt",
              "Oceania_Data.txt", "Antarctica_Data.txt", "Europa_Data.txt"]

# Specify the columns you want to include
columns_to_use = ["datetime", "value"]  # Replace with the actual column names you need

# Read each .txt file with only the specified columns and store them in a list of DataFrames
dataframes = [pd.read_csv(file, delimiter=" ", usecols=columns_to_use) for file in file_paths]

# Concatenate all DataFrames into one
combined_df = pd.concat(dataframes, ignore_index=True)

# Convert the combined DataFrame to JSON
json_data = combined_df.to_json(orient="records")

# Save the JSON data to a .json file
with open('co2_international_data.json', 'w', encoding="utf-8") as json_file:
    json_file.write(json_data)

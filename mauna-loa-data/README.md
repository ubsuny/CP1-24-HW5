# Mauna Loa CO₂ Concentration - Flask Monthly Data Processing

This directory contains files and scripts to process and store monthly CO₂ concentration data collected via flask sampling at the Mauna Loa Observatory.

## Files in This Directory

1. **`flask_monthly_raw.txt`**: The original raw data file downloaded from the NOAA website, containing monthly CO₂ concentration data from flask sampling at the Mauna Loa Observatory.
2. **`flask_monthly.py`**: Python script to process the raw data file. This script:
   - Loads the raw data, skipping metadata rows and treating nonsensical values as NaN.
   - Extracts relevant columns, combining year and month to create a timestamp.
   - Saves the processed data as a CSV, JSON, JSON without NaN, and Markdown file (CSV, Markdown, and additional JSON files are generated only when running the script).
3. **`flask_monthly.json`**: JSON file with the processed monthly CO₂ concentration data, where each entry includes:
   - `Timestamp`: The date of the observation in ISO format.
   - `CO2 (ppm)`: The concentration of CO₂ in parts per million (ppm).
4. **`LICENSE.txt`**: License file detailing usage rights and permissions for the data and code.
5. **`NOTES.md`**: Additional notes on data processing, including any special considerations or information about the data source.

## Usage

To process the data, you can run the `flask_monthly.py` script, which will read from `flask_monthly_raw.txt` and produce the processed output files in multiple formats.

```bash
python flask_monthly.py
```

Running this script will generate:

- A CSV file (`flask_monthly.csv`)
- A JSON file (`flask_monthly.json`)
- A JSON file without NaN values (`flask_monthly_no_nan.json`)
- A Markdown file (`flask_monthly.md`)

## Example JSON Data
Here is a sample of the data format used in `flask_monthly.json`:
```
[
    {
        "Timestamp": "1969-08-01T00:00:00Z",
        "CO2 (ppm)": 322.51
    },
    {
        "Timestamp": "1969-09-01T00:00:00Z",
        "CO2 (ppm)": 321.36
    },
    ...
]
```
## License and Citation
The data is provided under the **Creative Commons Zero (CC0) 1.0 Universal Public Domain Dedication**. Please refer to the `LICENSE.txt` file for detailed usage rights.

**Citation:** Please acknowledge NOAA GML as the data provider in any publications that make use of this dataset.

## Additional Notes
See `NOTES.md` for specific information on data processing and any relevant considerations.

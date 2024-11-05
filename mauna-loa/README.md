# Mauna Loa Observatory CO₂ Data Processing

This repository contains data and scripts to process CO₂ concentration data collected from the Mauna Loa Observatory. The data includes various types of CO₂ measurements, such as discrete, monthly, daily, and hourly readings, stored in subdirectories corresponding to the sampling type.

## Directory Structure

There are six subdirectories in the main directory. Each subdirectory contains similar sets of files based on data sampled at different frequencies or formats (e.g., flask monthly, insitu daily). The subdirectories are as follows:

- `flask-discrete/`
- `flask-monthly/`
- `insitu-daily/`
- `insitu-hourly/`
- `insitu-monthly/`
- `surface-discrete/`

### File Types in Each Subdirectory

Each subdirectory contains the following files:
- **Data Files**:
  - `.csv`: Comma-separated values file with CO₂ concentration data.
  - `.json`: JSON format of the same data.
  - `_no_nan.json`: JSON file excluding rows with missing (NaN) values.
  - `.md`: Markdown file representation of the data.
  - `_raw.txt`: Original raw data file as downloaded from NOAA.

- **Scripts and Documentation**:
  - `.py`: Python script used to process the raw data file.
  - `_README.html`: Detailed README from NOAA, including data usage, license, and warnings.

## Usage

The scripts are designed to load, process, and save CO₂ concentration data for different sampling types, generating a CSV, JSON, JSON (without NaNs), and Markdown output for each dataset. The data files include:

- `Timestamp`: Date and time of the sample.
- `Fractional Year`: The year with a decimal representing the exact time within the year.
- `CO2 (ppm)`: CO₂ concentration in parts per million.
- `Standard Deviation (ppm)`: Measurement uncertainty.

### Examples of Processed Data

#### CSV Example

```csv
Timestamp, Fractional Year, CO2 (ppm), Standard Deviation (ppm)
2021-07-02T15:21:59Z, 2021.500384291, 417.8, 0.041
2021-07-04T15:22:01Z, 2021.5058638064, 416.95, 0.041
...

```

#### JSON Example

```
[
    {
        "Timestamp": "2021-07-02T15:21:59Z",
        "Fractional Year": 2021.500384291,
        "CO2 (ppm)": 417.8,
        "Standard Deviation (ppm)": 0.041
    },
    {
        "Timestamp": "2021-07-04T15:22:01Z",
        "Fractional Year": 2021.5058638064,
        "CO2 (ppm)": 416.95,
        "Standard Deviation (ppm)": 0.041
    }
    ...
]
```

#### Markdown Example

```
| Timestamp           | Fractional Year | CO2 (ppm) | Standard Deviation (ppm) |
|---------------------|-----------------|-----------|---------------------------|
| 2021-07-02T15:21:59Z | 2021.500384291  | 417.8     | 0.041                     |
| 2021-07-04T15:22:01Z | 2021.5058638064 | 416.95    | 0.041                     |
...
```

## Requirements

- Python 3.x
- `pandas` library for data manipulation

## How to Use
To process a new raw data file, navigate to the respective folder and run the Python script, for example:

```python flask_monthly.py```

This will produce the necessary CSV, JSON, JSON (no NaN), and Markdown files in the same folder.

## Linting Compliance
The Python scripts in this repository are `pylint` **compliant**. This ensures that the code follows best practices for readability,
maintainability, and style according to PEP8 standards. For consistent results, ensure that `pylint` is installed:

```pip install pylint```

To run `pylint` on a script, use, for example:

```pylint insitu-hourly.py```

## License and Citation
All data files are in the public domain under the **Creative Commons Zero (CC0) 1.0 Universal Public Domain Dedication**. Please see the `LICENSE` file in this repository for more information.


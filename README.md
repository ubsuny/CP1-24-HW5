# Greenhouse gas FFT

**Take the FFT of the CO2/methane data available at the [NOAA Global Monitoring Lab](https://gml.noaa.gov).**

This Homework is seperated into three task groups (data collection, data preparation, and data presentation)

## Task group 1 data collection (3 members)
Check the license for the available data and add an appropiate license / NOTES for the repository.
For the data use a common layout (columns and rows) and to add to the repository use `pandas.DataFrame.to_json` (see https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html)
- Collect the CO2 data of the Mount Lua observatory and store in the repository as a pandas dataframe (1 member due Monday 2pm)
- Collect the CO2 data in the same time range (minimum of 5 years) of one station on each continent available and store in the repository as a pandas dataframe (1 member due Wednesday 2pm)
- Collect the methane data in the same time range (minimum of 5 years) of one station on each continent available and store in the repository as a pandas dataframe (1 member due Wednesday 2pm)

## Task group 2 data preparation (6 members)
Work on one single data preparation module called `preparation.py`  that contains the following functions:
- function that reads in the json files from the data collection task and returns a pandas time series with the index being a datetime object and the data being the concentration of CO2 / methane (1 member due Wednesday 2pm)
All following functions should assume as an input a pandas time series with the index being a datetime object and the data being the concentration of CO2 / methane or its fourier equivalent (index: frequency; data: power spectrum)
- fft / inverse fft using numpy and calculating the actual frequency in useful units (1 member due Monday 2pm)
- for padding / unpadding the data including a way to set a reasonable padding value (either automagically or manual) (1 member due Wednesday 2pm)
- windowing / unwindowing with a selection of windows (1 member due Wednesday 2pm)
- that removes high / low frequency noise (1 member due Wednesday 2pm)
- determine the frequency of the peak(s) (1 member due Friday 2pm)

All functions must also include docstrings and unit tests in `test_preparation.py`

## Task group 3 data presentation (max 6 members)
Work on a single data analysis Jupyter notebook using functions from `preparation.py` that contain for each task below only *one plot*:

- combined plot of cleaned up and raw data by using some combination of waveform modification (which should include padding, windowing, taking the FFT, removing noise, inverse FFT, and undoing the window+padding) of the CO2 data of the Mount Lua observatory in the time domain (1 member due Friday 2pm)
- plot of cleaned up power spectrum by using some combination of waveform modification (which should include padding, windowing, taking the FFT, removing noise, inverse FFT, and undoing the window+padding) of the CO2 data of the Mount Lua observatory in the frequency domain that also highlights the peak(s) (1 member due Friday 2pm)
- combined plot of cleaned up and raw data by using some combination of waveform modification (which should include padding, windowing, taking the FFT, removing noise, inverse FFT, and undoing the window+padding) of the CO2 data on available continents in the time domain (1 member due Friday 2pm)
- combined plot of cleaned up power spectra by using some combination of waveform modification (which should include padding, windowing, taking the FFT, removing noise, inverse FFT, and undoing the window+padding) of the CO2 data on available continents in the frequency domain that also highlights the peak(s) (1 member due Friday 2pm)
- cleaned up and raw data by using some combination of waveform modification (which should include padding, windowing, taking the FFT, removing noise, inverse FFT, and undoing the window+padding) of the methane data on available continents in the time domain (1 member due Friday 2pm)
- cleaned up power spectra by using some combination of waveform modification (which should include padding, windowing, taking the FFT, removing noise, inverse FFT, and undoing the window+padding) of the methane data on available continents in the frequency domain that also highlights the peak(s) (1 member due Friday 2pm)


## Task group 4 maintainers (max 2 members)
- Reuse github actions for linting and unit tests
- Merge PR
- assign Reviews after member requests
  
---
## Grading

| Homework Points                  |                |              |            |
| -------------------------------- | -------------- | ------------ | ---------- |
|                                  |                |              |            |
| Interaction on project           |                |              |            |
| Category                         | min per person | point factor | max points |
| Commits                          | 1              | 1            | 1          |
| Pull requests                    | 1              | 4            | 4          |
| PR Accepted                      | 1              | 4            | 4          |
| Other PR reviewed (by request)   | 1              | 4            | 4          |     
| Issues                           | 1              | 1            | 1          | 
| Closed Issues                    | 1              | 1            | 1          |
| \# Conversations                 | 12             | 1/4          | 3          |
|                                  |                |              |            |
| Total                            |                |              | 18         |
|                                  |                |              |            |
| Shared project points            |                |              |            |
| \# Milestones                    | 12             | 1/4          | 3          |
|                                  |                |              |            |
| Total                            |                |              | 21         |
|                                  |                |              |            |
|                                  |                |              |            |
| Result                           |                |              |            |
| Task completion                  |                |              | 21         |
|                                  |                |              |            |
| Sum                              |                |              | 42         |

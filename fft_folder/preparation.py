"""
preperation.py
inverse fast fourie transform

the function analyze_signal inputs
signal, tim, use_filter, selec_filter
signal the data, tim means the span of time in sec that goes by,
use_filter just means if you want to filter out noise if you want to enter yes if not anything else works
selec_filter is where you enter your filter, for exapmple entering if you enter 0.1 the function finds the
largest freqency and only gives you the frequencies that are larger than 0.1 times the largest

the function analyze_signal outputs 
freq, magnitude, main_frequencies, use_filt
freq is the axis for the plot, magnitude is the amount of the freq thats in the signal,
main_frequencies are the values found when you use a filter, use_filt is just for the plot function


the function anze_revm_trnd
so this function does all the same things as the function before only finds a best fit function to try and
remove the overall trend in the signal data. it computs the following trends and finds the best fit by computing
and compairing their adjusted r^2 values. the trends include quadratic, cubic, quartic and exponential

"""
import pandas as pd
import os
import math as m
import numpy as np

def analyze_signal(signal, tim, use_filter, selec_filter):
    """finds the frequencies"""
    N = len(signal)
    fs = N/tim
    isfft = np.fft.fft(signal)
    freq = np.fft.fftfreq(N, 1/fs)

    use_filt = 0
    filt = 0.0
    yes_no = use_filter.strip().lower()
    if yes_no == 'yes':
        filt = selec_filter
        use_filt = 1

    magnitude = np.abs(isfft)
    threshold = filt * np.max(magnitude)
    main_frequencies = freq[magnitude > threshold]

    return freq, magnitude, main_frequencies, use_filt

def anze_revm_trnd(signal, tim, use_filter, selec_filter):
    """same as analyze_signal but removes overall trend"""
    N = len(signal)
    fs = N/tim
    ss_total = np.sum((signal['y'] - np.mean(signal['y']))**2)


    params_quadratic = np.polyfit(signal['x'], signal['y'], 2)
    y_quad = np.polyval(params_quadratic, signal['x'])

    res_quad = np.sum((signal['y'] - y_quad)**2)
    r_sq_quad = 1 - (res_quad / ss_total)
    r_quad_adj = 1 - ((1 - r_sq_quad) * (N - 1) / (N - 3))


    params_cubic = np.polyfit(signal['x'], signal['y'], 3)
    y_cubic = np.polyval(params_cubic, signal['x'])

    res_cub = np.sum((signal['y'] - y_cubic)**2)
    r_sq_cub = 1 - (res_cub / ss_total)
    r_cub_adj = 1 - ((1 - r_sq_cub) * (N - 1) / (N - 4))


    params_quartic = np.polyfit(signal['x'], signal['y'], 4)
    y_tic = np.polyval(params_quartic, signal['x'])

    res_tic = np.sum((signal['y'] - y_tic)**2)
    r_sq_tic = 1 - (res_tic / ss_total)
    r_tic_adj = 1 - ((1 - r_sq_tic) * (N - 1) / (N - 5))


    log_y = np.log(signal['y'])
    params_linear = np.polyfit(signal['x'], log_y, 1)
    y_linear = np.polyval(params_linear, signal['x'])

    ss_tot_ep = np.sum((log_y - np.mean(log_y))**2)
    ss_residual = np.sum((log_y - y_linear)**2)
    r_sq_ep = 1 - (ss_residual / ss_tot_ep)
    r_ep_adj = 1 - ((1 - r_sq_ep) * (N - 1) / (N - 2))

    find_sml = min(r_quad_adj, r_cub_adj, r_tic_adj, r_ep_adj)

    if find_sml == r_quad_adj:
        signalnew = signal['y'] - y_quad
    if find_sml == r_cub_adj:
        signalnew = signal['y'] - y_cubic
    if find_sml == r_tic_adj:
        signalnew = signal['y'] - y_tic
    else:
        A = np.exp(params_linear[1])
        B = params_linear[0]
        y_ep = A * np.exp(B * signal['x'])
        signalnew = signal['y'] - y_ep


    isfft = np.fft.fft(signalnew)
    freq = np.fft.fftfreq(N, 1/fs)

    use_filt = 0
    filt = 0.0
    yes_no = use_filter.strip().lower()
    if yes_no == 'yes':
        filt = selec_filter
        use_filt = 1

    magnitude = np.abs(isfft)
    threshold = filt * np.max(magnitude)
    main_frequencies = freq[magnitude > threshold]

    return freq, magnitude, main_frequencies, use_filt

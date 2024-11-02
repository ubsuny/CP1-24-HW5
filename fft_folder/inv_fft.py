"""
inv_fft.py
inverse fast fourie transform
"""
import pandas as pd
import os
import math as m
import numpy as np

def analyze_signal(signal, fs, use_filter, selec_filter):
    """creats a filtered fft"""
    N = len(signal)
    isfft = np.fft.fft(signal)
    bins = np.fft.fftfreq(N, 1/fs)

    use_filt = 0
    filt = 0.0
    yes_no = use_filter.strip().lower()
    if yes_no == 'yes':
        filt = selec_filter
        use_filt = 1

    magnitude = np.abs(isfft)
    threshold = filt * np.max(magnitude)
    main_frequencies = bins[magnitude > threshold]

    return bins, magnitude, main_frequencies, use_filt


"""
trying to now make a way to remove overall trend
using Adjusted R-squared to determine which fit is best then it auto does this for you
the modles in the function include liner polynomial cubic and exponential
"""

def anze_revm_trnd(signal, fs, use_filter, selec_filter):
    """creats a filtered fft"""
    N = len(signal)
    ss_total = np.sum((signal['y'] - np.mean(signal['y']))**2)


    params_poly = np.polyfit(signal['x'], signal['y'], 2)
    y_poly = np.polyval(params_poly, signal['x'])

    res_poly = np.sum((signal['y'] - y_poly)**2)
    r_sq_poly = 1 - (res_poly / ss_total)
    r_poly_adj = 1 - ((1 - r_sq_poly) * (N - 1) / (N - 3))


    params_cubic = np.polyfit(signal['x'], signal['y'], 3)
    y_cubic = np.polyval(params_cubic, signal['x'])

    res_cub = np.sum((signal['y'] - y_cubic)**2)
    r_sq_cub = 1 - (res_cub / ss_total)
    r_cub_adj = 1 - ((1 - r_sq_cub) * (N - 1) / (N - 4))


    params_quartic = np.polyfit(signal['x'], signal['y'], 4)
    y_qua = np.polyval(params_quartic, signal['x'])

    res_qua = np.sum((signal['y'] - y_qua)**2)
    r_sq_qua = 1 - (res_qua / ss_total)
    r_qua_adj = 1 - ((1 - r_sq_qua) * (N - 1) / (N - 5))


    log_y = np.log(signal['y'])
    params_linear = np.polyfit(signal['x'], log_y, 1)
    y_linear = np.polyval(params_linear, signal['x'])

    ss_tot_ep = np.sum((log_y - np.mean(log_y))**2)
    ss_residual = np.sum((log_y - y_linear)**2)
    r_sq_ep = 1 - (ss_residual / ss_tot_ep)
    r_ep_adj = 1 - ((1 - r_sq_ep) * (N - 1) / (N - 2))

    find_sml = min(r_poly_adj, r_cub_adj, r_qua_adj, r_ep_adj)

    if find_sml == r_poly_adj:
        signalnew = signal['y'] - y_poly
    if find_sml == r_cub_adj:
        signalnew = signal['y'] - y_cubic
    if find_sml == r_qua_adj:
        signalnew = signal['y'] - y_qua
    else:
        A = np.exp(params_linear[1])
        B = params_linear[0]
        y_ep = A * np.exp(B * signal['x'])
        signalnew = signal['y'] - y_ep


    isfft = np.fft.fft(signalnew)
    bins = np.fft.fftfreq(N, 1/fs)

    use_filt = 0
    filt = 0.0
    yes_no = use_filter.strip().lower()
    if yes_no == 'yes':
        filt = selec_filter
        use_filt = 1

    magnitude = np.abs(isfft)
    threshold = filt * np.max(magnitude)
    main_frequencies = bins[magnitude > threshold]

    return bins, magnitude, main_frequencies, use_filt

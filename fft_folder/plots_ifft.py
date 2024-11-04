"""
plots_ifft.py

preperation.py
inverse fast fourie transform

the function analyze_signal inputs
signal, tim, use_filter, selec_filter
signal the data, tim means the span of time in sec that goes by,
use_filter just means if you want to filter out noise if you want to enter yes if not
anything else works
selec_filter is where you enter your filter, for exapmple entering if you enter 0.1 the
function finds the largest freqency and only gives you the frequencies that are larger
than 0.1 times the largest

the function analyze_signal outputs 
freq, magnitude, main_frequencies, use_filt
freq is the axis for the plot, magnitude is the amount of the freq thats in the signal,
main_frequencies are the values found when you use a filter, use_filt is just for the plot function


the function anze_revm_trnd
so this function does all the same things as the function before only finds a best fit function to
try and remove the overall trend in the signal data. it computs the following trends and finds the
best fit by computing and compairing their adjusted r^2 values. the trends include quadratic,
cubic, quartic and exponential

I will deleate this file this will be used for me for checking
if my code is funtioning proprly
"""
import os
import numpy as np
import matplotlib.pyplot as plt

def plot_rets(freq, magnitude,):
    """will deleate"""
    plt.figure(figsize=(12, 8))
    
    plt.plot(freq, magnitude, label=' wods')
    plt.title('Original data')
    plt.xlabel(' [1/s]')
    plt.ylabel('Your units of concern')
    plt.xlim(0, max(freq)/2)
    plt.legend()

    plt.tight_layout()

    plot = input("Do you want to save the plot? (yes/no): ").strip().lower()

    if plot == 'yes':
        fpath = input("enter where to save: ").strip()
        if not os.path.exists(fpath):
            print("Directory does not exist, try again")
        else:
            filpath = os.path.join(fpath, "workin it.png")
            plt.savefig(filpath, format='png', dpi=600)
            print(f"Plot saved as {filpath}")
    else:
        print("Plot not saved.")




def anze_revm_trnd(signal, tim, use_filter, selec_filter):
    """keeping this for now for adj r^2 calc"""
    n = len(signal)
    ss_total = np.sum((signal['y'] - np.mean(signal['y']))**2)


    params_quadratic = np.polyfit(signal['x'], signal['y'], 2)
    y_quad = np.polyval(params_quadratic, signal['x'])

    res_quad = np.sum((signal['y'] - y_quad)**2)
    r_sq_quad = 1 - (res_quad / ss_total)
    r_quad_adj = 1 - ((1 - r_sq_quad) * (n - 1) / (n - 3))


    params_cubic = np.polyfit(signal['x'], signal['y'], 3)
    y_cubic = np.polyval(params_cubic, signal['x'])

    res_cub = np.sum((signal['y'] - y_cubic)**2)
    r_sq_cub = 1 - (res_cub / ss_total)
    r_cub_adj = 1 - ((1 - r_sq_cub) * (n - 1) / (n - 4))


    params_quartic = np.polyfit(signal['x'], signal['y'], 4)
    y_tic = np.polyval(params_quartic, signal['x'])

    res_tic = np.sum((signal['y'] - y_tic)**2)
    r_sq_tic = 1 - (res_tic / ss_total)
    r_tic_adj = 1 - ((1 - r_sq_tic) * (n - 1) / (n - 5))


    log_y = np.log(signal['y'])
    params_linear = np.polyfit(signal['x'], log_y, 1)
    y_linear = np.polyval(params_linear, signal['x'])

    ss_tot_ep = np.sum((log_y - np.mean(log_y))**2)
    ss_residual = np.sum((log_y - y_linear)**2)
    r_sq_ep = 1 - (ss_residual / ss_tot_ep)
    r_ep_adj = 1 - ((1 - r_sq_ep) * (n - 1) / (n - 2))

    find_sml = min(r_quad_adj, r_cub_adj, r_tic_adj, r_ep_adj)

    if find_sml == r_quad_adj:
        signalnew = signal['y'] - y_quad
    if find_sml == r_cub_adj:
        signalnew = signal['y'] - y_cubic
    if find_sml == r_tic_adj:
        signalnew = signal['y'] - y_tic
    else:
        y_ep = (np.exp(params_linear[1])) * np.exp((params_linear[0]) * signal['x'])
        signalnew = signal['y'] - y_ep


    isfft = np.fft.fft(signalnew)
    freq = np.fft.fftfreq(n, tim/n)

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
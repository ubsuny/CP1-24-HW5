import unittest
import numpy as np
import pandas as pd
from noise_removal import remove_noise

class TestRemoveNoise(unittest.TestCase):
    def setUp(self):
        # Generate a synthetic time series with a mix of low and high-frequency components
        date_range = pd.date_range(start="2020-01-01", periods=100, freq="D")
        
        # Low-frequency component (e.g., sine wave with a low frequency)
        low_freq_component = np.sin(2 * np.pi * 0.01 * np.arange(100))
        
        # High-frequency component (e.g., random noise or a higher frequency sine wave)
        high_freq_component = 0.5 * np.sin(2 * np.pi * 0.3 * np.arange(100))
        
        # Combined data with both low and high frequencies
        data_values = low_freq_component + high_freq_component
        self.data = pd.Series(data_values, index=date_range)

    def test_remove_low_frequency(self):
        # Remove frequencies below 0.02 (should remove the low frequency component)
        filtered_data = remove_noise(self.data, low_freq=0.02, high_freq=None)
        
        # Verify that filtered data no longer contains low frequencies
        self.assertIsNotNone(filtered_data, "Filtered data is None")
        self.assertTrue((np.abs(np.fft.fft(filtered_data.values)[:10]) < 0.1).all(),
                        "Low-frequency components were not removed correctly")

    def test_remove_high_frequency(self):
        # Remove frequencies above 0.02 (should retain only the low frequency component)
        filtered_data = remove_noise(self.data, low_freq=None, high_freq=0.02)
        
        # Verify that filtered data no longer contains high frequencies
        self.assertIsNotNone(filtered_data, "Filtered data is None")
        self.assertTrue((np.abs(np.fft.fft(filtered_data.values)[20:]) < 0.1).all(),
                        "High-frequency components were not removed correctly")

    def test_full_bandpass_filter(self):
        # Apply both a low and high frequency filter to keep only a specific frequency range
        filtered_data = remove_noise(self.data, low_freq=0.01, high_freq=0.05)
        
        # Verify that filtered data is not None and contains frequencies within the specified range
        self.assertIsNotNone(filtered_data, "Filtered data is None")
        fft_values = np.abs(np.fft.fft(filtered_data.values))
        freqs = np.fft.fftfreq(len(filtered_data), d=(filtered_data.index[1] - filtered_data.index[0]).total_seconds())
        
        # Check that frequencies outside the range are close to zero
        self.assertTrue((fft_values[np.abs(freqs) < 0.01] < 0.1).all(), "Low frequencies not removed correctly")
        self.assertTrue((fft_values[np.abs(freqs) > 0.05] < 0.1).all(), "High frequencies not removed correctly")

if __name__ == '__main__':
    unittest.main()

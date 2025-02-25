import numpy as np

def fourier_transform(signal):
    return np.fft.fft(signal)

signal = [0, 1, 0, -1] * 4
transformed_signal = fourier_transform(signal)
print(transformed_signal)

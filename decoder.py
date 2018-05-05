# This file is to decode messages from audio recording in realtime.

import numpy as np
import scipy.io.wavfile
from scipy.signal import spectrogram,medfilt

filename = "test-001.wav"
audio_sample = scipy.io.wavfile.read(filename)
sampling_rate = audio_sample[0]
audio_sample = audio_sample[1][:,0]

f, t, sxx = spectrogram(audio_sample,sampling_rate,nperseg=2048,noverlap=32,window='blackman')

sxx = np.log10(sxx)

import matplotlib.pyplot as plt

'''
plt.pcolormesh(t, f[:10], sxx[:10,:],cmap='Greys_r')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.colorbar()
plt.show()
'''

# Seconds
pulse_length = 8

kernel = np.zeros(pulse_length * sampling_rate / 2048, dtype=float)
l = len(kernel)
kernel[:] = -1.0
kernel[l/2:] = 1.0

compressed_freq_range = sxx[:,:]
compressed_freq_range = np.sum(compressed_freq_range,axis=0)

convolved = np.convolve(kernel,compressed_freq_range)

med_filtered = medfilt(compressed_freq_range,kernel_size=177)
plt.plot(med_filtered)
plt.show()
